import cairo
import time
import numpy as np
import random
from helpers import *

SURFACE_X = SURFACE_Y = 1200
ITERS = 2

def draw_line(ctx, starting_pos, length, tilt, color=[0, 0, 0]):
    x0, y0 = starting_pos
    x1, y1 = x0 + np.cos(tilt) * length, y0 + np.sin(tilt) * length
    x2, y2 = x1 + np.tan(tilt) * length, y1 + np.tan(tilt) * length
    ctx.move_to(x0, y0)
    ctx.line_to(x1, y1)
    ctx.line_to(x2, y2)
    ctx.set_source_rgba(*color)
    ctx.fill()

def replace_line(line):
    starting_pos, length, tilt = line
    x0, y0 = starting_pos
    x1, y1 =  x0 + np.cos(tilt) * length, y0 + np.sin(tilt) * length
    x2, y2 = x1 + np.tan(tilt) * length, y1 + np.tan(tilt) * length
    line1 = [starting_pos, length, tilt]
    line2 = [(x1, y1), length, tilt/2 ]
    line3 = [(x2, y2), length / np.sqrt(2), tilt * 3]
    return([line1, line2, line3])

def generate_fractal(ctx, num_iter):
    lines = [[(100, 100), get_surface_center(SURFACE_X), random.random()]]
    for i in range(0, num_iter):
        new_lines = []
        for x in lines: 
            new_lines += replace_line(x)
        lines = new_lines
    for l in lines:
        draw_line(ctx, *l, color = generate_random_color())

def main():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_X, SURFACE_Y)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    generate_fractal(ctx, ITERS)
    surface.write_to_png("gallery/fractal_lines"+str(ITERS)+"_"+str(round(time.time() * 1000))+".png")

if __name__ == "__main__":
    main()