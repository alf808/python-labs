'''
Create a script that asks a user to input an integer, checks for the
validity of the input type, and displays a message depending on whether
the input was an integer or not.

The script should keep prompting the user until they enter an integer.

'''
while True:
    try:
        user_input = int(input("Please enter an integer: "))
    except ValueError:
        print("It must be an integer input.")
        continue
    else:
        print("you have entered an integer. bye")
        break