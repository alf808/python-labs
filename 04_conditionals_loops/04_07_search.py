'''

Receive a number between 0 and 1,000,000,000 from the user.
Use while loop to find the number - when the number is found exit the loop and print the number to the console.

'''
count = 0
print("This application will print your number when it is found.")
user_input = int(input("Please enter a number between 0 and 1000000000: "))
while count <= user_input:
    if count == user_input:
        print(count)
        break
    count += 1