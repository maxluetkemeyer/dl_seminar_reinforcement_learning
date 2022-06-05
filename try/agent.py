import random
import tensorflow as tf


class Agent():
    def __init__(self, strategy, num_actions):
        self.current_step = 0
        self.strategy = strategy
        self.num_actions = num_actions
    
    def select_action(self, state, policy_net):
        rate = self.strategy.get_exploration_rate(self.current_step)
        self.current_step += 1

        if rate > random.random():
            # explore
            action = random.randrange(self.num_actions)
            return tf.constant([action], dtype=tf.int32)
        else:
            # exploit
            # with torch.no_grad():
            #return policy_net(state).argmax(dim=1).item() 

            # get highest q value from model to select action
            # input is the state
            # use model only for inferrence and not for training
            # turn of gradient tracking - info in blog

            action = random.randrange(self.num_actions)
            return tf.constant([action], dtype=tf.int32)
