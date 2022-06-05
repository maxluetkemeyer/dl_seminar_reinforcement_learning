import matplotlib
import matplotlib.pyplot as plt
import tensorflow as tf

from cartpole_env_manager import CartPoleEnvManager

em = CartPoleEnvManager()
em.reset()
# screen = em.render(mode="rgb_array")

# plt.figure()
# plt.imshow(screen)
# plt.title("Non-processed screen example")
# plt.show()


# =====
screen = em.get_processed_screen()

plt.figure()
plt.imshow(tf.transpose(tf.squeeze(screen, 0), perm=[1, 2, 0]), interpolation="none")
plt.title("Processed screen example")
plt.show()