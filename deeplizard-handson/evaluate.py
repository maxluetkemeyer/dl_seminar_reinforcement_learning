import tensorflow as tf
import tensorflow.keras as keras
import numpy as np
import os
import datetime

from agent import Agent
from strategy import AlwaysExploitStrategy
from env import createEnviornment

keras.backend.clear_session()
tf.random.set_seed(42)
np.random.seed(42)

time_string = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
log_dir = "logs/" + time_string

input_shape = [4] # == env.observation_space.shape
n_actions = 2 # == env.action_space.n
n_episodes = 6000


policy_model = keras.models.load_model("models/20220608-162450.h5")
env = createEnviornment()
strategy = AlwaysExploitStrategy()
agent = Agent(num_actions=n_actions, strategy=strategy)


env.seed(42)

train_summary_writer = tf.summary.create_file_writer(log_dir)

os.system('clear')
for episode in range(1, n_episodes+1):
    state = env.reset()    
    for step in range(200):
        env.render(mode="human")
        
        action = agent.select_action(state, policy_model)
        next_state, reward, done, info = env.step(action)
        
        state = next_state
        if done:
            break

    with train_summary_writer.as_default():
        tf.summary.scalar('#Steps - Evaluate', step, step=episode)

    print("Episode: {}, Steps: {}".format(episode, step + 1))
    

