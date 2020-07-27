'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
with open("words.txt", "r") as fin:
    temp = fin.readline()
    new_temp = temp.replace(' ', '')
    if len(new_temp) > 20:
        print(temp)