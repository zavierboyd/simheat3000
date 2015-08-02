from __future__ import division
__author__ = 'zavidan'
from heat_simulation import *
import matplotlib.pyplot as plt
y = House([[0, 269.2656], [269.2656, 0]], [[1/278666.667], [1/45600.0]]).matrix_simulation([[17.0], [20.0]], 1)
x = range(len(y[0]))

walls = plt.plot(x, y[0], label="walls")
air = plt.plot(x, y[1], label="air")
plt.legend()
plt.title("The change in temperature")
plt.xlabel("Seconds (s)")
plt.ylabel("Temperature (C)")
plt.show()
