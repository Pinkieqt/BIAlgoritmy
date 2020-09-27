from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-500, 500)
Y = np.arange(-500, 500)
X, Y = np.meshgrid(X, Y)

d = 2

sum_sq_term = X*np.sin(np.sqrt(np.absolute(X))) + Y*np.sin(np.sqrt(np.absolute(Y)))

Z = 418.9829  *d + sum_sq_term 

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()