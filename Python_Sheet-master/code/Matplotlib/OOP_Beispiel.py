import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)

t = np.arange(100)/100
s1 = np.sin(2*np.pi*t)
s2 = s1 + np.random.randn(*s1.shape)/4
# Figure und Axis erstellen
fig, ax = plt.subplots()
# Signale plotten
ax.plot(t, s1, linestyle='-', marker='.', color="blue", label='Simulation')
# ax.plot(t, s1, '.-', label='Simulation')
ax.plot(t, s2, '.-', label='Messung')
# Achsen beschriften
ax.set_xlabel('Zeit (s)', fontsize=15)
ax.set_ylabel('Amplitude', fontsize=15)
# Achsen limitieren
ax.set_ylim(-1.5, 1.5)
# ax.set_xticks(np.arange(0, 1.1, step=0.1))
ax.set_xlim(0, 1)

ax.xaxis.set_major_locator(MultipleLocator(0.25))
ax.xaxis.set_minor_locator(MultipleLocator(0.05))
# Hilfslinien aktivieren
# ax.grid(True)
ax.grid(which="both")
# Legende hinzufuegen
ax.legend(loc="lower left")
# Weisser Rand minimieren
fig.tight_layout()