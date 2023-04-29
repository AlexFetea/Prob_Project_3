import numpy as np
import matplotlib.pyplot as plt

# Constants
tau = 57  # inches
a = 1 / tau

# PDF function
def f_X(x, a):
    return a**2 * x * np.exp(-(a**2 * x**2) / 2)

# CDF function
def F_X(x, a):
    return 1 - np.exp(-(a**2 * x**2) / 2)

# x_p values for given probability p
def x_p(p, a):
    return np.sqrt((-2 / a**2) * np.log(1 - p))

# PDF and CDF plot
x_values = np.linspace(0, 3 * tau, 500)
# plt.plot(x_values, f_X(x_values, a), label='PDF f_X(x)')
plt.plot(x_values, F_X(x_values, a), label='CDF F_X(x)')
plt.xlabel('x')
plt.ylabel('Probability')
plt.legend()
plt.show()

# Circle plot
probabilities = [0.5, 0.7, 0.9]
colors = ['r', 'g', 'b']
labels = ['p = 0.5', 'p = 0.7', 'p = 0.9']
T = (0, 0)

fig, ax = plt.subplots()
for p, color, label in zip(probabilities, colors, labels):
    circle = plt.Circle(T, x_p(p, a), color=color, fill=False, label=label)
    ax.add_artist(circle)

ax.set_xlim(-3 * tau, 3 * tau)
ax.set_ylim(-3 * tau, 3 * tau)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('East')
ax.set_ylabel('North')
plt.legend()
plt.show()