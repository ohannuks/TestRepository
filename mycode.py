import numpy as np
import pylab as plt

x = np.linspace(0,100,100)
y = np.cos(x)

plt.plot(x,y)
plt.savefig("test.pdf")
plt.close()
