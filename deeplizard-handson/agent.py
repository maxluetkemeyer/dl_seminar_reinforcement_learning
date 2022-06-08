import numpy as np
import tensorflow as tf

class Agent():
    def __init__(self, strategy, num_actions):
        self.current_step = 0
        self.strategy = strategy
        self.num_actions = num_actions
    
    def select_action(self, state, policy_model):
        rate = self.strategy.get_exploration_rate(self.current_step)
        self.current_step += 1

        if rate > np.random.rand():
            # explore
            action = np.random.randint(low=0, high=self.num_actions)
            return action
        else:
            # exploit
            Q_values = policy_model.predict(state[np.newaxis])
            return np.argmax(Q_values[0])
