import matplotlib.pyplot as plt
import numpy as np

import random

from prism import InclinedTriangularPrism


if __name__ == '__main__':
    plt.figure(figsize=(9, 9))
    
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

    for i in range(15, 8, -2):
        prism = InclinedTriangularPrism((0, 0), 'green')
        prism.scale(i)
        prism.draw()

    plt.show()
