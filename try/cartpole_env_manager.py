from operator import mod
import gym
import tensorflow as tf
import numpy as np

class CartPoleEnvManager():
    def __init__(self):
        self.env = gym.make("CartPole-v1").unwrapped #access to behind the scences dynamics
        self.env.reset()
        self.current_state = None
        self.done = False
    
    def reset(self):
        self.current_state = self.env.reset()

    def close(self):
        self.env.close()

    def render(self, mode="human"):
        return self.env.render(mode)

    def num_actions_available(self):
        return self.env.action_space.n

    def take_action(self, action):
        action = action.numpy()[0]

        self.current_state, reward, self.done, _ = self.env.step(action)
        return tf.constant([reward], dtype=tf.float32)

    def get_state(self):
        if self.done:
            return tf.zeros_like(tf.constant(self.current_state), dtype=tf.float32)
        else:
            return tf.constant(self.current_state, dtype=tf.float32)
    
    def num_state_features(self):
        return self.env.observation_space.shape[0]
