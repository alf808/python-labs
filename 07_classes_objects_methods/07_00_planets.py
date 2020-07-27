'''
Create a Planet class that models attributes and methods of
a planet object.

Use the appropriate dunder method to get informative output with print()

'''

class Planet():
    """Planet class models attributes and methods of planet object."""

    def __init__(self, name, color, shape):
        """Constructor with attributes"""
        self.name = name
        self.color = color
        self.shape = shape
    
    def __str__(self):
        return f"Planet {self.name} is {self.color} and {self.shape}"

earth = Planet('Earth', 'blue', 'spherical')
print(earth)
