'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.
circle
area = pi * radius**2
circum = 2 * pi * radius
radius = diameter / 2
'''
PI = 3.14159
def radius_circle(diameter):
    return diameter / 2

def area(diameter):
    radius = radius_circle(diameter)
    return PI * radius**2
    
def circumference(diameter):
    radius = radius_circle(diameter)
    return 2 * PI * radius

def sphere_surface_area(diameter):
    return 4 * area(diameter)
    
    