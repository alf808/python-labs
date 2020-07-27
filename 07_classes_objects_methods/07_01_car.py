'''
Write a class to model a car. The class should:

1. Set the attributes model, year, and max_speed in the __init__() method.
2. Have a method that increases the max_speed of the car by 5 when called.
3. Have a method that prints the details of the car.

Create at least two different objects of this Car class and demonstrate
changing the objects attributes.

'''
class Car:
    """class that models a car object"""

    def __init__(self, model, year, max_speed):
        self.model = model
        self.year = year
        self.max_speed = max_speed

    def __str__(self):
        return f"The car {self.year} {self.model} has max speed {self.max_speed}."

    def accelerate(self):
        """increases speed by 5"""
        self.max_speed += 5

toy = Car('Toyota', 1975, '45 mph')
maz = Car('Mazda', 2020, '37.2 mph')

print(toy)
print(maz)
