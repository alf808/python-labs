'''
Print out every prime number between 1 and 100.

'''
for num in range(2, 101):
    num_is_prime = True # assume num is prime
    for i in range(2, num):
        if num % i == 0:
            num_is_prime = False
            break # out of this for loop
    if num_is_prime:
        print(num)