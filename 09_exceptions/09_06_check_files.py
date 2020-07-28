'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import os

script_path = os.path.dirname(os.path.realpath(__file__))
books_path = os.path.join(script_path, "books")
file_name = 'integers.txt'
file = f"{script_path}/{file_name}"

with open(file, "r") as fin:
    temp_list = fin.readlines()
    for num in temp_list:
        try:
            x = int(num) / 7
        except TypeError:
            print("type error")
        except ValueError:
            print("not an integer")
        except IOError as ioe:
            print(f"got this error message: {ioe}")
        else:
            print(x)