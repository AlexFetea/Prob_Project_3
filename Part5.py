import random
import math
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm




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

    fig, axes = plt.subplots(2, 2, figsize=(10, 10))
    axes = axes.flatten()

    for index, tuple in enumerate(analyses):
        ax = axes[index]
        z_values = []
        values, mean, var = getMeanAndVar(tuple[0], tuple[1])
        print(mean, var)
        for value in values:
            z_values.append((value - mean)/math.sqrt(var))
        z = [-1.4, -1.0, -0.5, 0, 0.5, 1.0, 1.4]
        empirical_CDFs = [sum(map(lambda i: i <= num, z_values))/len(z_values) for num in z]
        standard_CDFs = [norm.sf(-num) for num in z]

        # Calculate the MAD
        temp = [abs(emp - std) for emp, std in zip(empirical_CDFs, standard_CDFs)]
        MAD = max(temp)
        print("-----------------------")
        concatenated_string = ' & '.join([f'{num:.4f}' for num in temp])
        print(concatenated_string)
        print(MAD)
        print("-----------------------")

        # Plot the empirical CDF points
        ax.scatter(z, empirical_CDFs, label='Empirical CDF', color='red', zorder=2)

        # Plot the standard CDF as a continuous function
        standard_CDFs_x = [i * 5 / 100 - 2.5 for i in range(100)]
        standard_CDFs_y = [norm.cdf(x) for x in standard_CDFs_x]
        ax.plot(standard_CDFs_x, standard_CDFs_y, label='Standard CDF', color='blue')

        # Create the highlighted region above and below the standard CDF line
        upper_bound = [y + MAD for y in standard_CDFs_y]
        lower_bound = [y - MAD for y in standard_CDFs_y]
        ax.fill_between(standard_CDFs_x, lower_bound, upper_bound, color='green', alpha=0.1, label='MAD')

        # Set up the axis labels and legend
        ax.set_title(str(tuple))
        ax.set_xlabel('z')
        ax.set_ylabel('Values')
        ax.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()

run_trials()