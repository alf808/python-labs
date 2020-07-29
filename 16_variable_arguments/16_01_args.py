'''
Write a script with a function that demonstrates the use of *args.

'''
def print_this(*args):
    for input in args:
        print(input)

def sum_this(*args):
    total = 0
    for num in args:
        total += num
    return total

print_this(35, 78, 21, 99999, 87)

print(sum_this(35, 78, 21, 99999, 87))