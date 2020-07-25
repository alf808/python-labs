'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple

If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

Note: This lab might be challenging! Make sure to discuss it with your mentor
or chat about it on our forum.

'''
result_list = []
temp = [5, 9, 1, 4, 7, 6, 3]
temp.sort()
if len(temp) % 2 != 0:
    temp.append(0)

for x in range(len(temp)//2):
    i, j = temp.pop(0), temp.pop(0)
    result_list.append((i,j))

print(result_list)