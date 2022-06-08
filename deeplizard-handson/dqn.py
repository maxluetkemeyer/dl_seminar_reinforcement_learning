import tensorflow as tf
import tensorflow.keras as keras

def createDQN(input_shape=[4], n_outputs=2) -> keras.Model:
    return keras.models.Sequential([
        keras.layers.Dense(32, activation="elu", input_shape=input_shape),
        keras.layers.Dense(32, activation="elu"),
        keras.layers.Dense(n_outputs)
    ])