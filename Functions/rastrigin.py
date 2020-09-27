from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5.12, 5.12)
Y = np.arange(-5.12, 5.12)
X, Y = np.meshgrid(X, Y)

d = 2

sum_sq_term = X*X + Y*Y - 10*np.cos(d*np.pi*X) - 10*np.cos(d*np.pi*Y)

Z = sum_sq_term + 10*d

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()