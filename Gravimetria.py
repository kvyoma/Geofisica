import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 1)
G = 6.74*(10**(-11))
Pe = 1000
Ps = 2000
r = 1000
z1 = 10000
z2 = 11000
z3 = 12000

def f(z):
	f = (4/3) * np.pi * G * (r**3) * (Pe - Ps) * (((z/x**2) + (z**2))**(3/2))
	return f

fig = plt.figure()
plt.plot(x, f(z1), label = 'z = 1000')
plt.plot(x, f(z2), label = 'z = 1100')
plt.plot(x, f(z3), label = 'z = 1200')
plt.xlim(-0.3, 0.3)
plt.legend()
plt.ylabel(r"Anomalia Gravitacional")
plt.show()
