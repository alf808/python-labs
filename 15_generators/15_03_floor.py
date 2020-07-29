'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

If I am reading the problem right,
I believe we get the quotient from dividend and divisor 1111
'''
gen_ = (i for i in range(70000) if i % 1111 == 0)
for i in gen_:
    print(i//1111) # get the quotient from dividend i and divisor 1111