import string
import random


def generate_random_string(length):
    random_string = "".join(random.choice(string.ascii_letters) for _ in range(length))
    return random_string
