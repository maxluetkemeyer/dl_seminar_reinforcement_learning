import time
import flappy_bird_gym
import gym

env = flappy_bird_gym.make("FlappyBird-v0")
#env = gym.make("FrozenLake-v0")

obs = env.reset()
while True:
    action = env.action_space.sample()

    obs, reward, done, info = env.step(action)

    env.render()
    time.sleep(1 / 15)

    if done:
        break

env.close()