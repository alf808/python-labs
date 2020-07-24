'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
print("This application will count the number of vowels.")
words = input("Please enter a string of words: ")
words = words.lower()

print(f"a: {words.count('a')}, e: {words.count('e')}, i: {words.count('i')}, o: {words.count('o')}, u: {words.count('u')}")

