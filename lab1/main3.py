import matplotlib.pyplot as plt
import numpy as np

import random

from prism import InclinedTriangularPrism


if __name__ == '__main__':
    plt.figure(figsize=(9, 9))
    
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

    for i in range(10, 5, -1):
        prism = InclinedTriangularPrism((-2, -2), 'green')
        prism.scale(i)
        prism.draw()

    plt.show()
