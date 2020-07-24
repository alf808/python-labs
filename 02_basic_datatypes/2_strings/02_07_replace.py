'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''
print("This application will replace all occurences of first letter in string with a symbol.")
words = input("Please enter a string of words: ")
symbol = input("Please enter a symbol: ")

first_char = words[0]
new_string = words.replace(first_char, symbol)

print(new_string)