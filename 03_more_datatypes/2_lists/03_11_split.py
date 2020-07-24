'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''
most_frequent_count = 0
most_frequent_word = ""

print("This application will give you the most frequent word in a string.")
temp = input("Please enter string: ")
string_list = temp.split()

for word in string_list:
    temp_count = string_list.count(word)
    if temp_count > most_frequent_count:
        most_frequent_count = temp_count
        most_frequent_word = word

print(f"The word with most occurences is \'{most_frequent_word}\'")