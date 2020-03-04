import matplotlib.pyplot as plt
import numpy as np

import random


class InclinedTriangularPrism:
    COLORS = {
            0: 'red',
            1: 'green',
            2: 'yellow',
            3: 'blue',
            4: 'purple',
            5: 'violet',
            6: 'orange'
        }

    def __init__(self, center, color):
        self.c = center
        self.points = np.array([
                        [self.c[0],       self.c[1]    ], 
                        [self.c[0] + 1,   self.c[1]    ], 
                        [self.c[0] + 0.7, self.c[1] + 1], 
                        [self.c[0] + 1,   self.c[1] + 3], 
                        [self.c[0] + 2,   self.c[1] + 3], 
                        [self.c[0] + 1.7, self.c[1] + 4]
                    ])
        self.color = color

    def draw(self):
        lines = []

        p = self.points
        lines.append(plt.plot([p[0][0], p[1][0]], [p[0][1], p[1][1]], marker='o', linestyle='-', color=self.color))
        lines.append(plt.plot([p[1][0], p[2][0]], [p[1][1], p[2][1]], marker='o', linestyle='--', color=self.color))
        lines.append(plt.plot([p[2][0], p[0][0]], [p[2][1], p[0][1]], marker='o', linestyle='--', color=self.color))

        lines.append(plt.plot([p[3][0], p[4][0]], [p[3][1], p[4][1]], marker='o', linestyle='-', color=self.color))
        lines.append(plt.plot([p[4][0], p[5][0]], [p[4][1], p[5][1]], marker='o', linestyle='-', color=self.color))
        lines.append(plt.plot([p[5][0], p[3][0]], [p[5][1], p[3][1]], marker='o', linestyle='-', color=self.color))

        lines.append(plt.plot([p[0][0], p[3][0]], [p[0][1], p[3][1]], marker='o', linestyle='-', color=self.color))
        lines.append(plt.plot([p[1][0], p[4][0]], [p[1][1], p[4][1]], marker='o', linestyle='-', color=self.color))
        lines.append(plt.plot([p[2][0], p[5][0]], [p[2][1], p[5][1]], marker='o', linestyle='--', color=self.color))

        return lines
    
    def rotate(self):
        self.points = self.points.dot(
            [[0, 1], 
             [-1, 0]])
    
    def scale(self, size):
        self.points = self.points.dot(
            [[size, 0],
             [0, size]]
        )

    @staticmethod
    def draw_rand_figures(count):
        for i in range(count):
            center = random.randint(-10, 10), random.randint(-10, 10)
            prism = InclinedTriangularPrism(
                center, 
                color=InclinedTriangularPrism.COLORS[random.randint(0, len(InclinedTriangularPrism.COLORS) - 1)]
                )
            prism.scale(random.randint(1, 5))
            prism.draw()
