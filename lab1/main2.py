import matplotlib.pyplot as plt
import numpy as np

import random

from prism import InclinedTriangularPrism


if __name__ == '__main__':
    plt.figure(figsize=(9, 9))
    
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

    InclinedTriangularPrism.draw_rand_figures(50) 

    plt.show()
