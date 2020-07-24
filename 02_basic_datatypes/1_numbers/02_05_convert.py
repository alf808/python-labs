'''

Demonstrate how to:

    1) Convert an int to a float
    2) Convert a float to an int
    3) Perform floor division using a float and an int.
    4) Use two user inputted values to perform multiplication.

    Take note of what information is lost when some conversions take place.

'''
# 1: convert an int to a float
num_int_to_float = float(41)
print(num_int_to_float)

# 2: convert float to int
num_float_to_int = int(4.1)
print(num_float_to_int)

# floor division with float and int

print(5.0//3)

# Use two user inputted values to perform multiplication

num1 = float(input(f"Please enter a number: "))
num2 = float(input(f"Please enter another number: "))
print(num1*num2)