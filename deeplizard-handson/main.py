import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import os
import datetime

from replay_memory import ReplayMemory
from dqn import createDQN
from agent import Agent
from strategy import EpsilonGreedyStrategy
from env import createEnviornment

keras.backend.clear_session()
tf.random.set_seed(42)
np.random.seed(42)

time_string = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = "logs/" + time_string

input_shape = [4] # == env.observation_space.shape
n_actions = 2 # == env.action_space.n
batch_size = 32
discount_rate = 0.95
n_episodes = 6000
target_update = 50
optimizer = keras.optimizers.Adam(learning_rate=1e-2)
loss_fn = keras.losses.mean_squared_error


policy_model = createDQN(input_shape=input_shape, n_outputs=n_actions)
target_model:keras.Model = keras.models.clone_model(policy_model)
target_model.set_weights(policy_model.get_weights())

replay_memory = ReplayMemory(2000)
env = createEnviornment()
strategy = EpsilonGreedyStrategy(start=1, end=0.01, decay=0.001)
agent = Agent(num_actions=n_actions, strategy=strategy)


rewards = [] 
best_score = 0
env.seed(42)

def train_step():
    states, actions, rewards, next_states, dones = replay_memory.sample(batch_size)

    next_Q_values = target_model.predict(next_states)
    max_next_Q_values = np.max(next_Q_values, axis=1)
    target_Q_values = (rewards +
                    (1 - dones) * discount_rate * max_next_Q_values)
    target_Q_values = target_Q_values.reshape(-1, 1)
    mask = tf.one_hot(actions, n_actions)
    with tf.GradientTape() as tape:
        all_Q_values = policy_model(states)
        Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
        loss = tf.reduce_mean(loss_fn(target_Q_values, Q_values))
    grads = tape.gradient(loss, policy_model.trainable_variables)
    optimizer.apply_gradients(zip(grads, policy_model.trainable_variables))


train_summary_writer = tf.summary.create_file_writer(log_dir)

best_score = 0

os.system('clear')
for episode in range(1, n_episodes+1):
    state = env.reset()    
    for step in range(200):
        #env.render(mode="human")
        
        action = agent.select_action(state, policy_model)
        next_state, reward, done, info = env.step(action)
        replay_memory.push(state, action, reward, next_state, done)
        
        state = next_state
        if done:
            break

    if episode > 50:
        if step >= best_score:
            policy_model.save("models/{}.h5".format(time_string))
            best_score = step

        train_step()

    with train_summary_writer.as_default():
        tf.summary.scalar('#Steps', step, step=episode)

    if episode % target_update == 0:
        target_model.set_weights(policy_model.get_weights())
        print("Episode: {}, Steps: {}, target_model weights updated".format(episode, step + 1))
    else:
        print("Episode: {}, Steps: {}".format(episode, step + 1))
    

