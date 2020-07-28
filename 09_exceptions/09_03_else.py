'''
Write a script that demonstrates a try/except/else.

'''
while True:
    try:
        user_input1 = int(input("Please enter first number: "))
        user_input2 = int(input("Please enter second number: "))
        print(user_input1 / user_input2)
    except ZeroDivisionError as zde:
        print(f"\nwhy do this: {zde}\n")
    except ValueError:
        print("\nYou were told to enter numbers!\n")
    else:
        print("\nYou followed instructions. Let\'s do this again. OK!")