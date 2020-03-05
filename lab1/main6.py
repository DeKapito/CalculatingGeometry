import math
import random

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
from prism import InclinedTriangularPrism


class ElipseAnimatedPrism:
    def __init__(self):
        self.scale = 2

        self.prism = InclinedTriangularPrism((0, 0), 'red')
        self.prism.scale(self.scale)

        self.fig = plt.figure(figsize=(9, 9))
        self.speed = 0.2
        self.scale_counter = 1

        self.x = 30
        self.y = 0

        plt.xlim(-40, 40)
        plt.ylim(-40, 40)
    
    def animate_circle(self):
        return FuncAnimation(self.fig, self.elips_move, frames=100, blit=True)

    def elips_move(self, i):
        self.prism.set_center((self.x, self.y))
        
        new_x = 10 * math.cos(i*self.speed)
        if new_x < self.x:
            self.prism.scale(self.scale_counter)
            self.scale_counter += 0.1
        elif new_x >= self.x:
            self.prism.scale(self.scale_counter)
            self.scale_counter -= 0.1

        self.x = new_x
        self.y = 5 * math.sin(i*self.speed)
        
        
        return self.prism.draw()


if __name__ == '__main__':
    anim_prism = ElipseAnimatedPrism()
    animation = anim_prism.animate_circle()
    plt.show()
