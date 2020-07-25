'''
Use a "while" loop to print out every fifth number counting from 1 to 1000.

'''
count = 1
while count <= 1000:
    if count % 5 == 0:
        print(count)
    count += 1