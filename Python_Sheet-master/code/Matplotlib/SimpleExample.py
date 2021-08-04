import numpy as np
import matplotlib.pyplot as plt

# signale definieren
t = np.arange(100)/100
s1 = np.sin(2*np.pi*t)
s2 = s1 + np.random.randn(*s1.shape)/4
# Figure und Axis erstellen
plt.figure()
# Signale plotten
plt.plot(t, s1, '.-', label='Simulation')
plt.plot(t, s2, '.-', label='Messung')
# Achsen beschriften
plt.xlabel('Zeit (s)')
plt.ylabel('Amplitude')
# Hilfslinien aktivieren
plt.grid(True)
# Legende hinzufuegen
plt.legend()
# Weisser Rand minimieren
plt.tight_layout()
# Diagramm abspeichern
plt.savefig('diagramm.svg')