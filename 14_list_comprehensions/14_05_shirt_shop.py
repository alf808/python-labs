'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''
# code based on https://stackoverflow.com/questions/52192855/cartesian-product-of-two-lists-in-python/52192888
colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]
products = [f"{color} in {size}" for color in colors for size in sizes]
print(products)