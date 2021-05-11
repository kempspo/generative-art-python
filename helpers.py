import random

def generate_random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    a = random.random()
    if a != 0:
        return([r, g, b, a])
    else:
        # regenerate
        print("Have to regenerate alpha is {a}".format(a))
        generate_random_color()

def get_surface_center(SURFACE_LEN):
    # assumes that its always a square
    x1 = x2 = SURFACE_LEN / 2
    return( (x1 + x2) / 2 )