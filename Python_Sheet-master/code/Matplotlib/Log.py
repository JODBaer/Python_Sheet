import numpy as np
import matplotlib.pyplot as plt

x = np.logspace(-2, 1, 20)
s = np.exp(-x)
# loglog-----------------------------------
fig, ax = plt.subplots()
ax.loglog(x, s, '-o', linewidth=2)
ax.grid(which='major')
ax.grid(which='minor')
ax.set_xlabel('Frequency (f)', fontsize=15)
ax.set_ylabel('Amplitude (V)', fontsize=15)
fig.tight_layout()
# semilogx---------------------------------
fig, ax = plt.subplots()
ax.semilogx(x, s, '-o', linewidth=2)
ax.grid(which='major')
ax.grid(which='minor')
ax.set_xlabel('Frequency (f)', fontsize=15)
ax.set_ylabel('Amplitude (V)', fontsize=15)
fig.tight_layout()
# semilogy---------------------------------