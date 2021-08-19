import numpy as np
import matplotlib.pyplot as plt

N = 100000
data = np.random.randn(N)

fig, axes = plt.subplots(3, sharex=True)
axes[0].hist(data, bins=100)
axes[0].set_title('Gausssches Histogramm', fontsize=18)
axes[0].set_xlabel('Wert', fontsize=14)
axes[0].set_ylabel('Anzahl', fontsize=14);

axes[1].hist(data, bins=100, density = True)
axes[1].set_title('Wahrscheinlichkeitsdichte', fontsize=18)
axes[1].set_xlabel('Wert', fontsize=14)
axes[1].set_ylabel('Haeufigkeit', fontsize=14);

axes[2].hist(data, bins=100, density = True, cumulative=True)
axes[2].set_title('Verteilungsfunktion', fontsize=18)
axes[2].set_xlabel('Wert', fontsize=14)
axes[2].set_ylabel('Kumulierte Haeufigkeit', fontsize=14);