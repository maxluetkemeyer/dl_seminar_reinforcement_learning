import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import gym
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime

log_dir = "logs/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

from replay_memory import ReplayMemory
from agent import Agent
from strategy import EpsilonGreedyStrategy
from dqn import createDQN
from env import createEnviornment

keras.backend.clear_session()
tf.random.set_seed(42)
np.random.seed(42)

env = createEnviornment()
env.seed(42)
input_shape = [4] # == env.observation_space.shape
n_outputs = 2 # == env.action_space.n

model = createDQN()

replay_memory = ReplayMemory(capacity=2000)
batch_size = 32
discount_rate = 0.95
optimizer = keras.optimizers.Adam(learning_rate=1e-2)
loss_fn = keras.losses.mean_squared_error

strat = EpsilonGreedyStrategy(start=1, end=0.01, decay=0.01)
agent = Agent(strategy=strat, num_actions=n_outputs)

def play_one_step(env, state, epsilon):
    action = agent.select_action(state=state,policy_model=model)

    next_state, reward, done, info = env.step(action)
    replay_memory.push(state, action, reward, next_state, done)

    return next_state, reward, done, info

def training_step(batch_size):
    experiences = replay_memory.sample(batch_size)
    states, actions, rewards, next_states, dones = experiences
    next_Q_values = model.predict(next_states)
    max_next_Q_values = np.max(next_Q_values, axis=1)
    target_Q_values = (rewards +
                       (1 - dones) * discount_rate * max_next_Q_values)
    target_Q_values = target_Q_values.reshape(-1, 1)
    mask = tf.one_hot(actions, n_outputs)
    with tf.GradientTape() as tape:
        all_Q_values = model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))
    grads = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads, model.trainable_variables))



train_summary_writer = tf.summary.create_file_writer(log_dir)


for episode in range(600):
    state = env.reset()    
    for step in range(200):
        #env.render(mode="human")
        epsilon = max(1 - episode / 500, 0.01)
        state, reward, done, info = play_one_step(env, state, epsilon)
        if done:
            break
    print("Episode: {}, Steps: {}, eps: {:.3f}".format(episode, step + 1, epsilon)) # Not shown
    if episode > 50:
        training_step(batch_size)

    with train_summary_writer.as_default():
        tf.summary.scalar('bsp', step, step=episode)
