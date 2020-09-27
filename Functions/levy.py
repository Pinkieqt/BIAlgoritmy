from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-10, 10)
Y = np.arange(-10, 10)
X, Y = np.meshgrid(X, Y)

wx = 1 + ( X - 1)/4
wy = 1 + ( Y - 1)/4

sin_term = np.sin(np.pi * X)*np.sin(np.pi * X)
sum_seq_term = (wx-1)*(wx-1)*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1))*(1 + 10*np.sin(np.pi*wx + 1)*np.sin(np.pi*wx + 1)) + (wy - 1)*(wy - 1)*(1 + np.sin(2*np.pi*wy)*np.sin(2*np.pi*wy))

Z = sin_term + sum_seq_term

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()