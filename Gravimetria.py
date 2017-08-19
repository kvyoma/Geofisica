import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5)
Pe = 2345
Ps = 4566
r = 1234
z = 6783

f = (4/3) * np.pi * G * (r**3) * (Pe - Ps) * (((z/x**2) + (z**2))**(3/2)) 
