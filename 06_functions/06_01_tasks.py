'''

Write a script that completes the following tasks.

'''

# define a function that determines whether the number is divisible by 4 or 7 and returns a boolean
def is_div_four_or_seven(num):
    if num % 7 == 0 or num % 4 == 0:
        return True
    else:
        return False

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean
def is_div_four_and_seven(num):
    if num % 7 == 0 and num % 4 == 0:
        return True
    else:
        return False
# take in a number from the user between 1 and 1,000,000,000
user_input = 21
# call your functions, passing in the user input as the arguments, and set their output equal to new variables 
output1 = is_div_four_or_seven(user_input)
output2 = is_div_four_and_seven(user_input)
# print your new variables to display the results
print(output1, output2)
