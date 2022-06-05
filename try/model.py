import tensorflow as tf
from tensorflow import keras

class DQN(keras.Model):
    def __init__(self, num_state_features, **kwargs):
        super().__init__(**kwargs)
        self.hidden1 = keras.layers.Dense(num_state_features)
        self.hidden2 = keras.layers.Dense(36, activation="relu")
        self.out = keras.layers.Dense(2)

    def call(self, inputs):
        
        Z = self.hidden1(inputs)
        print(self.hidden1.input_shape)
        Z = self.hidden2(inputs)
        return self.out(Z)

def createDQN(num_state_features):
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(32, activation="relu", input_shape=[num_state_features]))
    model.add(keras.layers.Dense(24, activation="relu"))
    model.add(keras.layers.Dense(2))
    return model
