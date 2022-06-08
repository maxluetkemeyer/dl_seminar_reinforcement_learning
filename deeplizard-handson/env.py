import gym

def createEnviornment() -> gym.Env:
    return gym.make("CartPole-v1")