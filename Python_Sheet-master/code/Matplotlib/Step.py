import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-2, 1, 20)
s = np.exp(-x)
fig, ax = plt.subplots()
x = np.arange(15)
y = np.array([0, 1, 3, 6, 10, 8, 7, 6, 5, -2, 2, 3, 1, 0, 2])
ax.step(x, y, '-o', where='pre');