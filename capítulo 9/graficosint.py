#matplotlib

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.random(50)*100
y = np.random.random(50)*100

plt.scatter(x,y,c='red',marker='d')

plt.show()

