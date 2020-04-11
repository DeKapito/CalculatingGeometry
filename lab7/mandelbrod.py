import numpy as np
import matplotlib.pyplot as plt

pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
ppoints, qpoints = 1000, 1000

max_iterations = 300
infinity_border = 10

image = np.zeros((ppoints, qpoints))

p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]

c = p + 1j*q
z = np.zeros_like(c)

for k in range(max_iterations):
    z = z**2 + c
    mask = (np.abs(z) > infinity_border) & (image == 0)
    image[mask] = k
    z[mask] = np.nan

plt.xticks([])
plt.yticks([])
plt.imshow(-image.T, cmap='flag', interpolation='bilinear')
plt.show()
