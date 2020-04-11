from tkinter import Tk, Canvas, BOTH, YES, ALL
import tkinter


class DragonFractal:
    def __init__(self, root):
        self.top_frame = tkinter.Frame(root)
        self.top_frame.pack(fill=BOTH, padx=5, pady=5)
        self.button = tkinter.Button(self.top_frame, text='Generate', command=self.generate_handler)
        self.button.pack(side=tkinter.RIGHT)
        self.scal = tkinter.Scale(
            self.top_frame, 
            orient=tkinter.HORIZONTAL, 
            length=500, 
            from_=0, 
            to=15, 
            tickinterval=5, 
            resolution=1, 
            label='Iterations')
        self.scal.pack()
        self.canvas = Canvas(root, width=800, height=800, background='white')
        self.canvas.pack(fill=BOTH, expand=YES)   

    def generate_handler(self):
        value = self.scal.get()
        self.draw_fractal(value)

    def draw_fractal(self, iterations):
        self.canvas.delete(ALL)
        self.draw(300, 300, 600, 600, iterations)

    def draw(self, x1, y1, x2, y2, iterations):
        if iterations > 0:
            xn = (x1 + x2) / 2 + (y2 - y1) / 2
            yn = (y1 + y2) / 2 - (x2 - x1) / 2
            self.draw(x2, y2, xn, yn, iterations - 1)
            self.draw(x1, y1, xn, yn, iterations - 1)

        if iterations == 0:
            self.canvas.create_line(x1, y1, x2, y2, fill='red', width=3)


if __name__ == "__main__":
    root = Tk()
    dragon = DragonFractal(root)
    dragon.draw_fractal(12)
    root.mainloop()
