'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
print("This application will translate a single name into pig latin.")
username = input("Please enter your name: ")
initial = username[0]
translated = username[1:] + initial + "ay"
print(f"{username} -> {translated}")