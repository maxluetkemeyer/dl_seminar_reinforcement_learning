from collections import namedtuple

# Experience class
Experience = namedtuple(
    "Experience",
    ("state", "action", "next_state", "reward")
)