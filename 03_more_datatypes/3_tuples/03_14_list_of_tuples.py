'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
input = "hello world"
input_list = input.split()
result_list = []

for word in input_list:
    temp_list = []
    for character in word:
        temp_list.append(character)
    temp_tuple = tuple(temp_list)
    result_list.append(temp_tuple)
print(result_list)