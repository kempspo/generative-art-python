import cairo
import time
import numpy as np
import random
import math
from helpers import *

SURFACE_X = SURFACE_Y = 1200
ITERS = 20


def draw_circle(ctx, color=[0, 0, 0]):
    x = round((random.random()) * SURFACE_X)
    y = round((random.random()) * SURFACE_Y)
    size = random.randint(0, SURFACE_X) / (random.random() * 10)
    if x < SURFACE_X and x > 0 and y < SURFACE_Y and y > 0:
        ctx.arc(x, y, size, 0, 2*math.pi)
        ctx.set_source_rgba(*color)
        ctx.fill()

def main():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_X, SURFACE_Y)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    for i in range(0, ITERS):
        draw_circle(ctx, color = generate_random_color())
    surface.write_to_png("gallery/circles"+str(ITERS)+"_"+str(round(time.time() * 1000))+".png")

if __name__ == "__main__":
    main()