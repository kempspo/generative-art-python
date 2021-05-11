import cairo
import time
import numpy as np
import math

SURFACE_X = SURFACE_Y = 1200
ITERS = 2

def get_surface_center():
    # assumes that its always a square
    x1 = x2 = SURFACE_X / 2
    return( (x1 + x2) / 2 )

def in_surface():
    """
    Returns a boolean whether or not the shape is within the surface area
    """
    pass

def draw_circle(ctx, color=[0, 0, 0]):
    ctx.arc(get_surface_center(), get_surface_center(), 50, 0, 2*math.pi)
    ctx.set_source_rgba(*color)
    ctx.fill()

def draw_triangle(ctx, color=[0, 0, 0]):
    ctx.move_to(240, 40)
    ctx.line_to(240, 160)
    ctx.line_to(350, 160)
    ctx.set_source_rgba(*color)
    ctx.fill()

def main():
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, SURFACE_X, SURFACE_Y)
    ctx = cairo.Context(surface)
    ctx.set_source_rgb(1, 1, 1)
    ctx.paint()
    draw_triangle(ctx)
    surface.write_to_png("gallery/shapes"+str(ITERS)+"_"+str(round(time.time() * 1000))+".png")

if __name__ == "__main__":
    main()