'''
Write a script that takes in two numbers from the user and calculates the quotient. Using a try/except,
the script should handle:

- if the user enters a string instead of a number
- if the user enters a zero as the divisor

Test it and make sure it does not crash when you enter incorrect values.

'''
while True:
    try:
        user_input1 = int(input("Please enter first number: "))
        user_input2 = int(input("Please enter second number"))

    except TypeError:
        print("that\'s not a number!")

    try:
        print(user_input1 / user_input2)
    except ZeroDivisionError as zde:
        print(f"why do this: {zde}")
