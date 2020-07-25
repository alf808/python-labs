'''
Use a loop to print the following table to the console:

 0 1 2 3 4 5 6 7 8 9
 10 11 12 13 14 15 16 17 18 19
 20 21 22 23 24 25 26 27 28 29
 30 31 32 33 34 35 36 37 38 39
 40 41 42 43 44 45 46 47 48 49

'''
count = 1
for x in range(50):
    if count < 10:
        print(x, end=" ")
        count += 1
    else:
        # print the last item in that line then start over into next line
        print(x)
        count = 1