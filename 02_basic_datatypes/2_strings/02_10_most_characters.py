'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
print("This application will ask you enter 3 strings and provide the number of characters in each word.")

#print(f"{len(str1)}, {str1}\n{len(str2)}, {str2}\n{len(str3)}, {str3}")
i = 0
longest_str_length = 0
longest_str = ""
str_list = []
while i < 3:
    str = input(f"Please enter string {i+1}: ")
    str_list.append(str)
    #print(f"{len(str)}, {str}\n")
    i += 1
    if len(str) > longest_str_length:
        longest_str_length = len(str)
        longest_str = str

print(f"\nThe string \'{longest_str}\' with {longest_str_length} characters has the most characters.")