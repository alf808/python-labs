'''
Write the necessary code calculate the volume and surface area
of a cylinder with a radius of 3.14 and a height of 5. Print out the result.


'''
# V = π r^2 h
# A = 2πrh + 2πr^2
pi = 3.14159
radius = 3.14
height = 5
cylinder_volume = pi * radius**2 * height
cylinder_surface_area = 2 * pi * radius * height + 2 * pi * radius**2
print(f"cylinder volume = {cylinder_volume}")
print(f"cylinder surface area = {cylinder_surface_area}")
