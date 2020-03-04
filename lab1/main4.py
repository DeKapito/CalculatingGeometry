import matplotlib.pyplot as plt
import numpy as np

import random

from matplotlib.animation import FuncAnimation
from prism import InclinedTriangularPrism

prism = InclinedTriangularPrism((0, 0), 'red')

def init():
    lines = prism.draw()
    print(lines)
    return prism.draw()

def x_move(i):
        prism.c = (prism.c[0] + i, prism.c[1])
        return prism.draw()


if __name__ == '__main__':
    fig = plt.figure(figsize=(9, 9))
    
    plt.xlim(-40, 40)
    plt.ylim(-40, 40)

    animation = FuncAnimation(fig, x_move, init_func=init, frames=10, blit=True)

    plt.show()
