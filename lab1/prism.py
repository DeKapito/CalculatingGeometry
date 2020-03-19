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
                        [self.c[0] - 1,   self.c[1] - 2], 
                        [self.c[0],       self.c[1] - 2], 
                        [self.c[0] - 0.3, self.c[1] - 1], 
                        [self.c[0],       self.c[1] + 1], 
                        [self.c[0] + 1,   self.c[1] + 1], 
                        [self.c[0] + 0.7, self.c[1] + 2]
                    ])
        self.color = color
    
    def set_center(self, center):
        x_diff = center[0] - self.c[0]
        y_diff = center[1] - self.c[1]
        self.c = center
        self.move((x_diff, y_diff))

    def get_borders(self):
        return {
            'top': self.points[5][1],
            'bottom': self.points[0][1],
            'right': self.points[4][0],
            'left': self.points[0][0],
        }
    
    def move(self, direct_coords, speed=1):
        for i in range(len(self.points)):
            self.points[i][0] += direct_coords[0]*speed
            self.points[i][1] += direct_coords[1]*speed

    def draw(self):
        lines = []

        p = self.points
        lines.append(plt.plot([p[0][0], p[1][0]], [p[0][1], p[1][1]], marker='o', linestyle='-', color=self.color)[0])
        lines.append(plt.plot([p[1][0], p[2][0]], [p[1][1], p[2][1]], marker='o', linestyle='--', color=self.color)[0])
        lines.append(plt.plot([p[2][0], p[0][0]], [p[2][1], p[0][1]], marker='o', linestyle='--', color=self.color)[0])

        lines.append(plt.plot([p[3][0], p[4][0]], [p[3][1], p[4][1]], marker='o', linestyle='-', color=self.color)[0])
        lines.append(plt.plot([p[4][0], p[5][0]], [p[4][1], p[5][1]], marker='o', linestyle='-', color=self.color)[0])
        lines.append(plt.plot([p[5][0], p[3][0]], [p[5][1], p[3][1]], marker='o', linestyle='-', color=self.color)[0])

        lines.append(plt.plot([p[0][0], p[3][0]], [p[0][1], p[3][1]], marker='o', linestyle='-', color=self.color)[0])
        lines.append(plt.plot([p[1][0], p[4][0]], [p[1][1], p[4][1]], marker='o', linestyle='-', color=self.color)[0])
        lines.append(plt.plot([p[2][0], p[5][0]], [p[2][1], p[5][1]], marker='o', linestyle='--', color=self.color)[0])

        return lines
    
    def rotate(self):
        self.points = self.points.dot(
            [[0, 1], 
             [-1, 0]])
    
    def scale(self, size):
        temp_center = self.c
        self.points = np.array([
                        [self.c[0] - 1,   self.c[1] - 2], 
                        [self.c[0],       self.c[1] - 2], 
                        [self.c[0] - 0.3, self.c[1] - 1], 
                        [self.c[0],       self.c[1] + 1], 
                        [self.c[0] + 1,   self.c[1] + 1], 
                        [self.c[0] + 0.7, self.c[1] + 2]
                    ])
        self.points = self.points.dot(
            [[size, 0],
             [0, size]]
        )
        self.set_center(temp_center)

    @staticmethod
    def draw_rand_figures(count):
        for i in range(count):
            while True:
                center = random.randint(-10, 10), random.randint(-10, 10)
                prism = InclinedTriangularPrism(
                    center, 
                    color=InclinedTriangularPrism.COLORS[random.randint(0, len(InclinedTriangularPrism.COLORS) - 1)]
                    )
                prism.scale(random.randint(1, 5))
                borders = prism.get_borders()
                if borders['top'] >= 40         \
                    or borders['bottom'] <= -40 \
                    or borders['right'] >= 40   \
                    or borders['left'] <= -40:
                    continue
                prism.draw()
                break
