from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(0, np.pi)
Y = np.arange(0, np.pi)
X, Y = np.meshgrid(X, Y)

m = 10

sum_sq_term = np.sin(X)*np.power(np.sin(X*X/np.pi), 2*m) + np.sin(Y)*np.power(np.sin(d*Y*Y/np.pi), 2*m)

Z = - sum_sq_term

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()