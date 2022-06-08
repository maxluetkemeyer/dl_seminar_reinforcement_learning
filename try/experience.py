from collections import namedtuple
import tensorflow as tf

# Experience class
Experience = namedtuple(
    "Experience",
    ("state", "action", "next_state", "reward")
)

def extract_tensors(experiences):
    batch = Experience(*zip(*experiences))
    t1 = tf.stack(batch.state)
    t2 = tf.concat(batch.action, axis=0)
    t3 = tf.concat(batch.reward, axis=0)
    t4 = tf.stack(batch.next_state)

    return (t1,t2,t3,t4)