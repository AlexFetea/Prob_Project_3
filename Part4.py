import random
import math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

n = 1000

random_state = 1000
rng_multiplier = 24693
rng_increment = 3967
rng_modulus = 2 ** 18

def get_next_random():
    global random_state
    random_state = (rng_multiplier * random_state + rng_increment) % rng_modulus
    return random_state / rng_modulus

def inverse_rayleigh(u):
    assert 0 <= u <= 1, "u is not in [0,1]"

    return math.sqrt(-2 * math.log(1 - u)) / 57

def run_trial():
    pass
    
def plot_stats():
    pass

def print_randoms():
    n = 0
    for i in range(50):
        n += 1
        get_next_random()

    n += 1
    print(n, get_next_random())
    n += 1
    print(n, get_next_random())
    n += 1
    print(n, get_next_random())
