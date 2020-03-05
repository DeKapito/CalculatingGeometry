import matplotlib.pyplot as plt
import numpy as np

import random

from matplotlib.animation import FuncAnimation
from prism import InclinedTriangularPrism


class AnimatedPrism:

    DIRECTIONS = {
        'right': (1, 0),
        'left': (-1, 0),
        'up': (0, 1),
        'down': (0, -1),
        'up_right': (1, 1),
        'down_left': (-1, -1)
    }

    def __init__(self):
        self.scale = 2

        self.prism = InclinedTriangularPrism((0, 0), 'red')
        self.prism.scale(self.scale)

        self.fig = plt.figure(figsize=(9, 9))
        self.speed = 4
        self.direction = 'right'

        self.min_limit = -40
        self.max_limit = 40

        plt.xlim(self.min_limit, self.max_limit)
        plt.ylim(self.min_limit, self.max_limit)

    def move(self, direction):
        move_coords = self.DIRECTIONS[direction]
        self.prism.move(move_coords, self.speed)

    def x_move(self, i):
        self.move(self.direction)

        if self.prism.get_borders()['right'] >= self.max_limit - 5:
            self.direction = 'left'
        elif self.prism.get_borders()['left'] <= self.min_limit + 5:
            self.direction = 'right'
        
        return self.prism.draw()
    
    def y_move(self, i):
        self.move(self.direction)

        if self.prism.get_borders()['top'] >= self.max_limit - 5:
            self.direction = 'down'
        elif self.prism.get_borders()['bottom'] <= self.min_limit + 5:
            self.direction = 'up'
        
        return self.prism.draw()
    
    def x_y_move(self, i):
        if self.direction == 'up_right':
            self.prism.scale(1.1)
        else:
            self.prism.scale(0.9)
        self.move(self.direction)

        if self.prism.get_borders()['top'] >= self.max_limit - 5:
            self.direction = 'down_left'
        elif self.prism.get_borders()['bottom'] <= self.min_limit + 5:
            self.direction = 'up_right'
        
        return self.prism.draw()
    
    def animate_x(self):
        self.direction = 'right'
        return FuncAnimation(self.fig, self.x_move, frames=100, blit=True)

    def animate_y(self):
        self.direction = 'up'
        return FuncAnimation(self.fig, self.y_move, frames=100, blit=True)
    
    def animate_x_y(self):
        self.direction = 'up_right'
        self.prism.set_center((-35, -35))
        return FuncAnimation(self.fig, self.x_y_move, frames=100, blit=True)


if __name__ == '__main__':
    anim_prism = AnimatedPrism()
    animation = anim_prism.animate_x_y()
    plt.show()
