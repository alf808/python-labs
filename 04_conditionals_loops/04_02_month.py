'''
Take in a number from the user and print "January", "February", ...
"December", or "Other" if the number from the user is 1, 2,... 12,
or other respectively. Use a "nested-if" statement.

'''
months = ["Jan", "Feb", "March", "April", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
print("This application will print the month that corresponds to a number.")
user_input = int(input("Please enter a number between 1 and 12: "))
if user_input in range(1,13):
    print(months[user_input-1])
else:
    print("Other")