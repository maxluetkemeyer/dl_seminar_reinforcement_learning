import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import os

from replay_memory import ReplayMemory
from dqn import createDQN
from agent import Agent
from strategy import EpsilonGreedyStrategy
from env import createEnviornment



input_shape = [4] # == env.observation_space.shape
n_actions = 2 # == env.action_space.n
batch_size = 32
discount_rate = 0.95
n_episodes = 600
target_update = 50
optimizer = keras.optimizers.Adam(learning_rate=1e-2)
loss_fn = keras.losses.mean_squared_error


policy_model = createDQN(input_shape=input_shape, n_outputs=n_actions)
target_model:keras.Model = keras.models.clone_model(policy_model)
target_model.set_weights(policy_model.get_weights())

replay_memory = ReplayMemory(10000)
env = createEnviornment()
strategy = EpsilonGreedyStrategy(start=1, end=0.01, decay=0.001)
agent = Agent(num_actions=n_actions, strategy=strategy)






rewards = [] 
best_score = 0

os.system('clear')
for episode in range(1, n_episodes+1):
    state = env.reset()    
    for step in range(200):
        #env.render(mode="human")
        
        action = agent.select_action(state, policy_model)
        next_state, reward, done, info = env.step(action)
        replay_memory.push(state, action, reward, next_state, done)

        if done:
            break
    
    print("Episode: {}, Steps: {}".format(episode, step + 1))
    
    if replay_memory.can_provide_sample(batch_size):
        experiences = replay_memory.sample(batch_size)
        states, actions, rewards, next_states, dones = experiences

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

    if episode % target_update == 0:
        target_model.set_weights(policy_model.get_weights())
        print("Target Model Weights updated")

