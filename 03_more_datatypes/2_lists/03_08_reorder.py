'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''
print("Enter 10 numbers 1 at a time and app will perform a sort of transformation.")

i = 0
num_str = []
num_str_pos_even = []

while i < 10:
    num = int(input(f"Please enter number {i+1}: "))
    if i % 2 == 0:
        num_str_pos_even.append(num)
    else:
        num_str.append(num)
    i += 1

num_str_pos_even.reverse()
transformed_list = num_str + num_str_pos_even
print(f"transformed: {transformed_list}")
