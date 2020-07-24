'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''
print("This application will multiply all the numbers you enter.")
print("Please enter one number at a time.")
i = 0
num_list = []
num_product = 1
while i < 10:
    num = float(input(f"Please enter number {i+1}: "))
    num_list.append(num)
    num_product *= num
    i += 1

print(f"max: {max(num_list)}")
print(f"product: {num_product}") 

