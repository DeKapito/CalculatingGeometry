import numpy as np
import matplotlib.pyplot as plt

from scipy import interpolate
from scipy.interpolate import interp1d


points = np.array([[1.5, 80],
                   [1.9, 136],
                   [2.3, 70],
                   [2.7, 165],
                   [3.1, 102]])
x = points[:,0]
y = points[:,1]

tck = interpolate.splrep(x, y, s=0)

x_new = np.arange(1.4, 3.3, 0.01)
y_new = interpolate.splev(x_new, tck, der=0)

plt.xlim([min(x) - 0.3, max(x) + 0.3])
plt.ylim([min(y) - 10, max(y_new) + 10])
plt.plot(x, y, 'o', x_new, y_new, color='blue')
plt.title('Cubic Spline')

plt.show()