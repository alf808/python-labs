'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''
gen_ = (i for i in range(70000) if i % 1111 == 0)
for i in gen_:
    print(i)