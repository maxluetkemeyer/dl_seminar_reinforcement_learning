import tensorflow as tf
import tensorflow.keras as keras
from itertools import count
import numpy as np

from cartpole_env_manager import CartPoleEnvManager
from epsilon_greedy_strategy import EpsilonGreedyStrategy
from agent import Agent
from replay_memory import ReplayMemory
from experience import Experience, extract_tensors
from model import DQN, createDQN
from q_values import QValues

batch_size = 256
gamma = 0.999
eps_start = 1
eps_end = 0.01
eps_decay = 0.001
target_update = 10 # every 10 epochs
memory_size = 100000
n_epochs = 1000

em = CartPoleEnvManager()
strategy = EpsilonGreedyStrategy(eps_start, eps_end, eps_decay)
agent = Agent(strategy, em.num_actions_available())
memory = ReplayMemory(memory_size)

policy_net = createDQN(em.num_state_features())
target_net = createDQN(em.num_state_features())
target_net.set_weights(policy_net.get_weights())
# target_net nur evaluate
optimizer = keras.optimizers.Adam(learning_rate=1e-2)
loss_fn = keras.losses.mean_squared_error



episode_durations = []
for epoch in range(1, n_epochs+1):
    print("Epoch {}/{}".format(epoch, n_epochs))
    em.reset()
    state = em.get_state()

    for timestep in count():
        em.render()

        action = agent.select_action(state, policy_net)
        reward = em.take_action(action)
        next_state = em.get_state()
        memory.push(Experience(state, action, next_state, reward))
        state = next_state

        if memory.can_provide_sample(batch_size):
            experiences = memory.sample(batch_size)
            states, actions, rewards, next_states = extract_tensors(experiences)

            """current_q_values = QValues.get_current(policy_net, states, actions)
            next_q_values = QValues.get_next(target_net, next_states)
            target_q_values = (next_q_values * gamma) + rewards

            # loss
            # optimizer
            # loss.backward()
            # optimizer.step()"""
            next_q_values = target_net.predict(next_states)
            max_next_q_values = np.max(next_q_values, axis=1)
            target_q_values = (rewards + gamma * max_next_q_values)

            target_q_values = target_q_values.reshape(-1, 1)
            mask = tf.one_hot(actions, 2)
            with tf.GradientTape as tape:
                all_q_values = policy_net(states)
                q_values = tf.reduce_sum(all_q_values * mask, axis=1, keepdims=True)
                loss = tf.reduce_mean(loss_fn(target_q_values, q_values))
            grads = tape.gradient(loss, policy_net.trainable_variables)
            optimizer.apply_gradients(zip(grads, policy_net.trainable_variables))

        if em.done:
            episode_durations.append(timestep)
            #plot(episode_durations, 100)
            break

    if epoch % target_update == 0:
        target_net.set_weights(policy_net.get_weights())

em.close()
