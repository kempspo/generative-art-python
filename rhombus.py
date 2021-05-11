import cairo
import numpy as np
import random
import time
from helpers import *

SURFACE_X = SURFACE_Y = 1500
ITERS = 2

def draw_rhombus(ctx, pos, length, tilt, ang_width, color=[0, 0, 0]):
    x0, y0 = pos
    x1, y1 = x0 + np.cos(tilt) * length, y0 + np.sin(tilt) * length
    x2, y2 = x1 + np.cos(tilt + ang_width) * length, y1 + np.sin(tilt + ang_width) * length
    x3, y3 = x0 + np.cos(tilt + ang_width) * length, y0 + np.sin(tilt + ang_width) * length
    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.line_to(x3, y3)
    ctx.line_to(x0, y0)
    ctx.set_source_rgba(*color)
    ctx.fill()

def replace_rhombus(rhomb):
    pos, length, theta, phi = rhomb
    x0, y0 = pos
    x1, y1 = x0 + np.cos(theta) * length, y0 + np.sin(theta) * length
    x3, y3 = x0 + np.cos(theta + phi) * length, y0 + np.sin(theta + phi) * length
    rhomb1 = [pos, length / np.sqrt(3), theta + phi/2, phi]
    rhomb2 = [(x3, y3), length / np.sqrt(3), theta - 3*phi/2, phi]
    rhomb3 = [(x1, y1), length / np.sqrt(3), theta + phi/2, phi]
    return([rhomb1, rhomb2, rhomb3])    

def generate_fractal(ctx, num_iter):
    rhombi = [[(275, 100), get_surface_center(), random.random(), np.pi/3]]
    for i in range(0, num_iter):
        new_rhombi = []
        for x in rhombi: 
            new_rhombi += replace_rhombus(x)
        rhombi = new_rhombi
    for r in rhombi:
        draw_rhombus(ctx, *r, color = generate_random_color())

def main():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_X, SURFACE_Y)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    print(get_surface_center())
    generate_fractal(ctx, ITERS)
    surface.write_to_png("gallery/rhomb_fractal_"+str(ITERS)+"_"+str(round(time.time() * 1000))+".png")

if __name__ == "__main__":
    main()