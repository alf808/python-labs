'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]

def stats(lst):
  # define the function here
  total = sum(lst)
  average = total / len(example_list)
  return max(lst), min(lst), average, total

# call the function below here
print(stats(example_list))