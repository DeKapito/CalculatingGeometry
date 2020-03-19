import matplotlib.pyplot as plt
import numpy as np

import random

from prism import InclinedTriangularPrism


if __name__ == '__main__':
    prism = InclinedTriangularPrism((0, 0), 'green')
    prism.scale(4)
    prism.draw()

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)



    plt.show()
