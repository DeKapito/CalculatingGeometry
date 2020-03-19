import math
import random

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
from prism import InclinedTriangularPrism
from matplotlib.patches import Ellipse


class ElipseAnimatedPrism:
    def __init__(self):
        self.scale = 2

        self.prism = InclinedTriangularPrism((0, 0), 'red')
        self.prism.scale(self.scale)

        self.fig = plt.figure(figsize=(9, 9))
        self.speed = 0.3
        self.scale_counter = self.scale

        self.x = 0
        self.y = 0

        plt.xlim(-40, 40)
        plt.ylim(-40, 40)
    
    def animate_circle(self):
        return FuncAnimation(self.fig, self.elips_move, frames=1000, blit=True)

    def elips_move(self, i):
        new_x = 10 * math.cos(i*self.speed)
        new_y = 5 * math.sin(i*self.speed)

        if new_y > self.y:
            self.scale_counter -= 0.15
        elif new_y < self.y:
            self.scale_counter += 0.15

        self.x = new_x
        self.y = new_y
        self.prism.scale(self.scale_counter)
        self.prism.set_center((self.x, self.y))
   
        return self.prism.draw()


if __name__ == '__main__':
    anim_prism = ElipseAnimatedPrism()
    ellipse = Ellipse((0, -5), width=30, height=20)
    ax = plt.gca()
    ax.add_patch(ellipse)
    animation = anim_prism.animate_circle()

    plt.show()
