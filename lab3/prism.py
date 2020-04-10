from tkinter import Tk, Canvas, BOTH, YES,ALL
from math import cos, sin

import numpy as np
import math
import copy
import itertools as it


class Vertex:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


class Prism:
    bg_color = 'white'

    def __init__(self, root):
        self.root = root
        self.init_data()
        self.create_canvas()
        self.draw_clock()
        self.draw_dimetric_projection()
        self.bind_mouse_buttons()

    def init_data(self):
        self.num_vertexes = 10

        self.heights = [125, 125, 120, 80, 40, 3, -3, -40, -80, -120, -125, -125]
        self.radiuses = [0, 125, 120, 100, 70, 5, 5, 70, 100, 120, 125, 0]
        
        angle_step = 2 * math.pi / self.num_vertexes
        vertexes = []
        for height, radius in zip(self.heights, self.radiuses):
            for i in range(0, self.num_vertexes):
                vertex = Vertex()
                vertex.x = math.cos(i * angle_step) * radius
                vertex.y = math.sin(i * angle_step) * radius
                vertex.z = height
                vertexes.append(vertex)

        self.points = np.array([[v.x, v.y, v.z] for v in vertexes]).transpose()

    def create_canvas(self):
        self.canvas = Canvas(
            self.root, width=800, height=800, background=self.bg_color)
        self.canvas.pack(fill=BOTH, expand=YES)

    def bind_mouse_buttons(self):
        self.canvas.bind("<Button-1>", self.on_mouse_clicked)
        self.canvas.bind("<B1-Motion>", self.on_mouse_motion)

    def draw_line(self, x1, y1, x2, y2, color='red'):
        w = self.canvas.winfo_width() / 2
        h = self.canvas.winfo_height() / 2
        if h < 1 and w < 1:
            h, w = 400, 400
        self.canvas.create_line(
            x1+w, h-y1, 
            x2+w, h-y2, 
            fill=color
            ) 

    def draw_clock(self):
        self.canvas.delete(ALL)
        colors = it.cycle(['red', 'blue', 'black', 'green'])
        color = next(colors)
        for i in range(1, len(self.points[0])+1):     
            source = i - 1
            target = i
            if i % self.num_vertexes == 0:
                target = i - self.num_vertexes
            self.draw_line(
                self.points[0][source], self.points[1][source],
                self.points[0][target], self.points[1][target],
                color=color
            )
            if i < len(self.points[0]) - self.num_vertexes:
                self.draw_line(
                    self.points[0][source], self.points[1][source],
                    self.points[0][source+self.num_vertexes], self.points[1][source+self.num_vertexes],
                    color=color
                )
            if i % self.num_vertexes == 0:
                color = next(colors)
    
    def draw(self, points):
        self.canvas.delete(ALL)
        colors = it.cycle(['red', 'blue', 'black', 'green'])
        color = next(colors)
        for i in range(1, len(points[0])+1):     
            source = i - 1
            target = i
            if i % self.num_vertexes == 0:
                target = i - self.num_vertexes
            self.draw_line(
                points[0][source], points[1][source],
                points[0][target], points[1][target],
                color=color
            )
            if i < len(points[0]) - self.num_vertexes:
                self.draw_line(
                    points[0][source], points[1][source],
                    points[0][source+self.num_vertexes], points[1][source+self.num_vertexes],
                    color=color
                )
            if i % self.num_vertexes == 0:
                color = next(colors)

    def draw_dimetric_projection(self):
        psi = 0.4
        fi = 0.4

        dimetric_matrix = np.array([
            [cos(psi), sin(fi)*sin(psi),    0], 
            [0,        cos(psi),            0], 
            [sin(psi), -sin(psi)*cos(psi),  0],
        ])
        
        points = np.dot(dimetric_matrix, self.points)
        self.draw(points)

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

    def on_mouse_clicked(self, event):
        self.last_x = event.x
        self.last_y = event.y

    def on_mouse_motion(self, event):
        dx = self.last_y - event.y
        self.points = self.rotate_along_x(-dx * 0.01, self.points)
        dy = self.last_x - event.x
        self.points = self.rotate_along_y(dy * 0.01, self.points)
        self.draw_dimetric_projection()
        self.on_mouse_clicked(event)


def main():
    root = Tk()
    Prism(root)
    root.mainloop()


if __name__ == '__main__':
    main()