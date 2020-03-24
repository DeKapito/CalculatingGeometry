from tkinter import Tk, Canvas, BOTH, YES,ALL
from math import cos, sin

import numpy as np


class Prism:
    fg_color = 'red'
    bg_color = 'white'

    def __init__(self, root):
        self.root = root
        self.init_data()
        self.create_canvas()
        self.draw_shapes_prism()
        # self.bind_mouse_buttons()
        self.continually_rotate()

    def init_data(self):
        self.prism = np.array([
            # bottom
            [-150,  100, -200],
            [50,   100, -200],
            [50,  -100, -200],
            [-50,    -200, -200],
            [-150, -100, -200],

            # top
            [-50,  100,  200],
            [150,   100,  200],
            [150,  -100,  200],
            [50,    -200,  200],
            [-50, -100,  200],
        ]).transpose()

        self.prism_lines = [
            (0, 1), (1, 2), (2, 3), (3, 4), (4, 0), # bottom 
            (5, 6), (6, 7), (7, 8), (8, 9), (9, 5), # top 
            (0, 5), (1, 6), (2, 7), (3, 8), (4, 9), # sides
        ]

        self.prism_shapes = [
            (0, 1, 2, 3, 4), (5, 6, 7, 8, 9),
            (0, 5, 9, 4), (0, 5, 6, 1),
            (1, 6, 7, 2), (3, 8, 7, 2),
            (4, 9, 8, 3),
        ]

    def create_canvas(self):
        self.canvas = Canvas(
            self.root, width=800, height=800, background=self.bg_color)
        self.canvas.pack(fill=BOTH, expand=YES)

    def bind_mouse_buttons(self):
        self.canvas.bind("<Button-1>", self.on_mouse_clicked)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)

    def draw_line(self, x1, y1, x2, y2):
        w = self.canvas.winfo_width() / 2
        h = self.canvas.winfo_height() / 2
        if h < 1 and w < 1:
            h, w = 400, 400
        self.canvas.create_line(
            x1+w, h-y1, 
            x2+w, h-y2, 
            fill=self.fg_color)

    def draw_shapes_prism(self):
        w = self.canvas.winfo_width() / 2
        h = self.canvas.winfo_height() / 2
        if h < 1 and w < 1:
            h, w = 200, 200
        self.canvas.delete(ALL)
        shapes = []
        for shape in self.prism_shapes:
            sum_z = 0
            points = []
            for vertex in shape:
                x = self.prism[0][vertex] + w
                y = h - self.prism[1][vertex]
                points.append((x, y))

                z = self.prism[2][vertex]
                sum_z += z

            shapes.append((points, sum_z/len(points)))
        
        shapes = sorted(shapes, key=lambda x: x[-1])
        for shape in shapes:
            points = []
            for point in shape[0]:
                points.append(point[0])
                points.append(point[1])
            self.canvas.create_polygon(points, outline='red', fill='yellow', width=2)

    def draw_cascade_prism(self):
        self.canvas.delete(ALL)
        
        w = self.canvas.winfo_width() / 2
        h = self.canvas.winfo_height() / 2
        if h < 1 and w < 1:
            h, w = 200, 200
        self.canvas.delete(ALL)

        for line in self.prism_lines:
            self.draw_line(
                self.prism[0][line[0]], self.prism[1][line[0]],
                self.prism[0][line[1]], self.prism[1][line[1]]
            )

    def rotate_along_x(self, x, figure):
        rotate_x_matrix = np.array([
            [1,    0,       0     ], 
            [0,    cos(x), -sin(x)], 
            [0,    sin(x),  cos(x)],
        ])
        return np.dot(rotate_x_matrix, figure)

    def rotate_along_y(self, y, figure):
        rotate_y_matrix = np.array([
            [cos(y),  0,   sin(y)], 
            [0,       1,   0     ], 
            [-sin(y), 0,   cos(y)],
        ])
        return np.dot(rotate_y_matrix, figure)
    
    def rotate_along_z(self, z, figure):
        rotate_z_matrix = np.array([
            [cos(z),  sin(z), 0], 
            [-sin(z), cos(z), 0], 
            [0,       0,      1],
        ])
        return np.dot(rotate_z_matrix, figure)

    def continually_rotate(self):
        # self.prism = self.rotate_along_x(0.03, self.prism)
        # self.prism = self.rotate_along_y(0.03, self.prism)
        self.prism = self.rotate_along_z(0.03, self.prism)
        self.draw_shapes_prism()
        self.root.after(15, self.continually_rotate)

    def on_mouse_clicked(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_mouse_motion(self, event):
        dx = self.last_y - event.y
        self.prism = self.rotate_along_x(-dx * 0.01, self.prism)
        dy = self.last_x - event.x
        self.prism = self.rotate_along_y(dy * 0.01, self.prism)
        self.draw_shapes_prism()
        self.on_mouse_clicked(event)


def main():
    root = Tk()
    Prism(root)
    root.mainloop()


if __name__ == '__main__':
    main()