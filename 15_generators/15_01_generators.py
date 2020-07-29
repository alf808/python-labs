'''
Demonstrate how to create a generator object. Print the object to the console to see what you get.
Then iterate over the generator object and print out each item.

'''
gen_ = (i for i in range(20))
for i in gen_:
    print(i)