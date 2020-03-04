import matplotlib.pyplot as plt
import numpy as np

import random


class InclinedTriangularPrism:
    def __init__(self, center):
        c = center
        self.points = np.array([
                        [c[0],       c[1]    ], 
                        [c[0] + 1,   c[1]    ], 
                        [c[0] + 0.7, c[1] + 1], 
                        [c[0] + 1,   c[1] + 3], 
                        [c[0] + 2,   c[1] + 3], 
                        [c[0] + 1.7, c[1] + 4]
                    ])

    def draw(self):
        p = self.points
        plt.plot([p[0][0], p[1][0]], [p[0][1], p[1][1]], marker='o', linestyle='-', color='green')
        plt.plot([p[1][0], p[2][0]], [p[1][1], p[2][1]], marker='o', linestyle='--', color='green')
        plt.plot([p[2][0], p[0][0]], [p[2][1], p[0][1]], marker='o', linestyle='--', color='green')
        
        plt.plot([p[3][0], p[4][0]], [p[3][1], p[4][1]], marker='o', linestyle='-', color='green')
        plt.plot([p[4][0], p[5][0]], [p[4][1], p[5][1]], marker='o', linestyle='-', color='green')
        plt.plot([p[5][0], p[3][0]], [p[5][1], p[3][1]], marker='o', linestyle='-', color='green')

        plt.plot([p[0][0], p[3][0]], [p[0][1], p[3][1]], marker='o', linestyle='-', color='green')
        plt.plot([p[1][0], p[4][0]], [p[1][1], p[4][1]], marker='o', linestyle='-', color='green')
        plt.plot([p[2][0], p[5][0]], [p[2][1], p[5][1]], marker='o', linestyle='--', color='green')
    
    def rotate(self):
        self.points = self.points.dot([[0, 1], [-1, 0]])
    
    def draw_rand_figures(self, count):
        for i in range(count):
            center = random.randint(-10, 10), random.randint(-10, 10)
            prism = InclinedTriangularPrism(center)
            prism.draw()


if __name__ == '__main__':

    # for points in [rectangle]:
    #     plt.plot(*zip(*(points + points[:1])), marker='o')

    prism = InclinedTriangularPrism((0, 0))
    prism.draw_rand_figures(50)

    plt.xlim(-20, 20)
    plt.ylim(-20, 20)



    plt.show()
