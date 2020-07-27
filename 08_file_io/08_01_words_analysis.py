'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
input_list = []
word_list = []
shortest_words = []
longest_words = []
shortest = 0
longest = 0
with open("words.txt", "r") as fin:
    # read all the words in to a list
    input_list = fin.readlines()
    # if line of string contains more than. assumption: only alphanumeric chars and whitespace
    # split the string into list
    for item in input_list:
        if len(item.split()) == 1:
            word_list.append(item)
        else:
            for w in item.split():
                word_list.append(w)

    # work with complete word_list
    for word in word_list:
        length = len(word)
        # test for shortest
        if length < shortest:
            shortest = length

        # test for longest
        if length > longest:
            longest = length

    # take the shortest and longest count
    for word in word_list:
        if len(word) == shortest:
            shortest_words.append(word)
        if len(word) == longest:
            longest_words.append(word)

    print("shortest words: " + shortest_words)
    print("longest words: " + longest_words)