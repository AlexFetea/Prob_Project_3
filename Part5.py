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

    return math.sqrt(-2 * math.log(1 - u)) * 57

def get_sample(size):
    values = []
    for _ in range(size):
        values.append(inverse_rayleigh(get_next_random()))

    return values


def getMeanAndVar(n, K):
    values = []
    for _ in range(K):
        sample_values = get_sample(n)
        sample_mean = sum(sample_values)/len(sample_values)
        values.append(sample_mean)

    mean = sum(values)/len(values)
    var = 0 
    for value in values:
        var+= value ** 2 - mean ** 2

    var/=len(values)

    return values, mean, var




def run_trials():
    analyses = [(3,5), (9,25), (27,110), (81, 550)]

    for tuple in analyses:
        z_values = []
        values, mean, var = getMeanAndVar(tuple[0], tuple[1])
        print(mean, var)
        for value in values:
            z_values.append((value - mean)/math.sqrt(var))

    

run_trials()
