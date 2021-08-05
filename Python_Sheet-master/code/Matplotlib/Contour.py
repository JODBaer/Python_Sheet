import numpy as np
import matplotlib.pyplot as plt
# contour-------------------------------
x = y = np.linspace(-2, 2, 11)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)
fig, ax = plt.subplots()
cont = ax.contour(X, Y, Z);
ax.clabel(cont, inline=True, fontsize=8);
# contourf------------------------------
x = y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X**2 + Y**2)*10

fig, ax = plt.subplots()
cont = ax.contourf(X, Y, Z, 20, cmap='inferno');
cbar = fig.colorbar(cont);
cbar.ax.set_ylabel('C');