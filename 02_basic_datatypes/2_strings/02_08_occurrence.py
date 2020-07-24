'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''
print("This application will find the index of first occurence of letter in string.")
words = input("Please enter a string of words: ")
letter = input("Please enter a letter to find: ")
pos_letter = words.find(letter)
print(f"The letter is at position {pos_letter}")
