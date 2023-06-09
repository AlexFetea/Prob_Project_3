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

def get_sample_mean(size):
    values = [inverse_rayleigh(get_next_random()) for _ in range(size)]
    return sum(values) / size

def run_trials():
    sample_sizes = [10, 30, 50, 100, 250, 500, 1000]
    X = []
    Y = []
    mu_x = 1/57 * math.sqrt(math.pi / 2)
    for size in sample_sizes:
        # 110 estimates of each sample mean
        for i in range(110):
            X.append(size)
            Y.append(get_sample_mean(size))
    plt.scatter(X, Y, s=2)
    plt.title("Sample Means of Rayleigh Distribution")
    plt.xlabel("Sample Size")
    plt.ylabel("Sample Mean")
    plt.plot([0, 1000], [mu_x, mu_x], color='r')
    plt.xscale('log')
    plt.show()
    
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

run_trials()
