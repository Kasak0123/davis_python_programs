# threeDfigures.py
import math

# Cube
def cube_surface_area(side):
    return 6 * side * side

def cube_volume(side):
    return side ** 3

# Cuboid
def cuboid_surface_area(l, b, h):
    return 2 * (l*b + b*h + l*h)

def cuboid_volume(l, b, h):
    return l * b * h

# Cylinder
def cylinder_curved_surface_area(r, h):
    return 2 * math.pi * r * h

def cylinder_total_surface_area(r, h):
    return 2 * math.pi * r * (r + h)

def cylinder_volume(r, h):
    return math.pi * r**2 * h

# Cone
def cone_curved_surface_area(r, l):
    return math.pi * r * l

def cone_total_surface_area(r, l):
    return math.pi * r * (l + r)

def cone_volume(r, h):
    return (1/3) * math.pi * r**2 * h

# Sphere
def sphere_surface_area(r):
    return 4 * math.pi * r**2

def sphere_volume(r):
    return (4/3) * math.pi * r**3

# Hemisphere
def hemisphere_curved_surface_area(r):
    return 2 * math.pi * r**2

def hemisphere_total_surface_area(r):
    return 3 * math.pi * r**2

def hemisphere_volume(r):
    return (2/3) * math.pi * r**3