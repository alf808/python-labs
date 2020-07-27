'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''
# assumption: single words per line
input_list =[]
word_list =[]
with open("words.txt", "r") as fin:
    input_list = fin.readlines()
    # take out newline characters
    word_list = [word.rstrip() for word in input_list]
    word_list.reverse()

with open("words_reverse.txt", "w") as fout:
    # write to file with newline characters
    fout.write("\n".join(word_list))
