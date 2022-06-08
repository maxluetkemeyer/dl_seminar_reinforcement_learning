import tensorflow as tf
import tensorflow.keras as keras
K = keras.backend

def createDQN(input_shape=[4], n_outputs=2) -> keras.Model:
    # DDQN (Dueling DQN algorithm)
    input_states = keras.layers.Input(shape=input_shape)
    hidden1 = keras.layers.Dense(32, activation="elu")(input_states)
    hidden2 = keras.layers.Dense(32, activation="elu")(hidden1)
    state_values = keras.layers.Dense(1)(hidden2)
    raw_advantages = keras.layers.Dense(n_outputs)(hidden2)
    advantages = raw_advantages - K.max(raw_advantages, axis=1, keepdims=True)
    q_values = state_values + advantages
    model = keras.Model(inputs=[input_states], outputs=[q_values])

    return model

    """return keras.models.Sequential([
        keras.layers.Dense(32, activation="elu", input_shape=input_shape),
        keras.layers.Dense(32, activation="elu"),
        keras.layers.Dense(n_outputs)
    ])"""