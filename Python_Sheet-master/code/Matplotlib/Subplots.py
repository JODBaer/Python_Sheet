import numpy as np
import matplotlib.pyplot as plt

t = np.arange(100)/100
s1 = np.sin(2*np.pi*t)
s2 = s1 + np.random.randn(*s1.shape)/4
# Figure und Axis erstellen
fig = plt.figure()
ax1 = plt.subplot(2, 1, 1)
ax2 = plt.subplot(2, 1, 2, sharex=ax1)
# Signale plotten
ax1.plot(t, s1, '.-', label='Simulation')
ax2.plot(t, s2, '.-', label='Simulation')
# Achsen beschriften
# ax1.set_xlabel('Zeit (s)', fontsize=12)
ax1.set_ylabel('Amplitude (v)', fontsize=12)
ax2.set_xlabel('Zeit (s)', fontsize=12)
ax2.set_ylabel('Amplitude (V)', fontsize=12)
# Achsen limitieren
ax1.set_ylim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax1.set_xlim(0, 1)
# Subplots beschriften
ax1.set_title("Simulation")
ax2.set_title("Measurement")
# Hilfslinien aktivieren
ax1.grid(True)
ax2.grid(True)
# Weisser Rand minimieren
fig.tight_layout()
##########################################
# Multiple subplots
fig, axes = plt.subplots(3, 2, sharex=True)
axes[0][0].plot(np.random.randn(10))
axes[0][1].plot(np.random.randn(10))
axes[1][0].plot(np.random.randn(10))
fig.tight_layout()