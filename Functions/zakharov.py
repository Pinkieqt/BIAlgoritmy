from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')

# Make data.
X = np.arange(-5, 10)
Y = np.arange(-5, 10)
X, Y = np.meshgrid(X, Y)

d = 2

first_sum_sq_term = X*X +Y*Y
second_sum_sq_term = (0.5*X + 0.5*d*Y)*(0.5*X + 0.5*d*Y)
third_sum_sq_term = (0.5*X + 0.5*d*Y)*(0.5*X + 0.5*d*Y)*(0.5*X + 0.5*d*Y)*(0.5*X + 0.5*d*Y)

Z = first_sum_sq_term + second_sum_sq_term + third_sum_sq_term

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

plt.show()