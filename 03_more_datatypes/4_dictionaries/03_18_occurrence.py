'''
Write a script that takes a string from the user and creates a dictionary of letter that exist
in the string and the number of times they occur. For example:

user_input = "hello"
result = {"h": 1, "e": 1, "l": 2, "o": 1}

'''
result = {}
user_input = "hello world"
trimmed_input = user_input.replace(' ', '')
for character in trimmed_input:
    result[character] = trimmed_input.count(character)

print(result)
