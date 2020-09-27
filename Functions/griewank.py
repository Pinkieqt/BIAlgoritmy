from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-600, 600)
Y = np.arange(-600, 600)
X, Y = np.meshgrid(X, Y)

sum_sq_term = (X*X + Y*Y)/4000
cos_term = np.cos(X) * np.cos(Y)/np.sqrt(2)

Z = sum_sq_term + cos_term + 1

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()