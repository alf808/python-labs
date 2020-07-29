'''
Write a script with a function that demonstrates the use of **kwargs.

'''
def cook_this(**kwargs):
    for k, v in kwargs.items():
        print(f"{k}: {v}")

cook_this(recipe="roast veggies", appliance="oven",
            temp=350, cook_time="2 hours",
            ingredients=['broccoli', 'carrots', 'cabbage', 'tomatoes'])