# Exercise to be turned in

import numpy as np
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt

#-------------------First subplot--------------------------
plt.subplot(1, 2, 1)

x = np.linspace(-10, 10, 1000)

#Powers are **, not ^.
y = x
plt.plot(x, y, 'r', label = "y = x")

y = x **2
plt.plot(x, y, 'g', label = "y = x^2")

y = x **3
plt.plot(x, y, 'b', label = "y = x^3")

plt.xlabel("Numbers")
plt.ylabel("Polynomials")

plt.legend(loc = "lower left")

plt.title("Normal graph you wanted")

#-------------------Second subplot--------------------------
plt.subplot(1, 2, 2, polar = True)

theta = np.linspace(-1, 1, 1000)

r = theta
plt.plot(r, theta, 'r', label = r" $ \theta = r $")

r = theta **2
plt.plot(r, theta, 'g', label = r" $ \theta = r^2 $")

r = theta **3
plt.plot(r, theta, 'b', label = r" $ \theta = r^3 $")

plt.legend(loc = "lower left")

plt.title("Polar graph you wanted")
		 
		 
#-------------------Final Setup-----------------------------

#plt.show()

plt.savefig("subplots.pdf")


