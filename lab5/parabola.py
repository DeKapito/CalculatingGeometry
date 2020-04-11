from tkinter import Tk, Canvas, PhotoImage, mainloop
from math import fabs

WIDTH, HEIGHT = 800, 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()
img = PhotoImage(width=WIDTH, height=HEIGHT)
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state="normal")

def set_pixel(x, y):
    img.put('black', (x + HALF_WIDTH, HALF_HEIGHT - y))

def parabola(x0=0, y0=0, p=4):
    x = y = 0

    Sd = ((y + 1)**2) - 2*p*(x + 1)
    Sv = ((y + 1)**2) - 2*p*x
    Sh = (y ** 2) - 2*p*(x + 1)

    while x + x0 < WIDTH:
        if Sh - Sv <= 0:
            if fabs(Sd) - fabs(Sh) < 0:
                y += 1
            x += 1
        else:
            if fabs(Sv) - fabs(Sd) > 0:
                x += 1
            y += 1

        set_pixel(x + x0, y + y0)
        set_pixel(x + x0, -y + y0)

        Sd = ((y + 1)**2) - 2*p*(x + 1)
        Sv = ((y + 1)**2) - 2*p*x
        Sh = (y ** 2) - 2*p*(x + 1)

parabola(-300, 0)
mainloop()
