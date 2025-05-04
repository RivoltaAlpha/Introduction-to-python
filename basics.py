# Description: This file contains the basic python code snippets.
# function in python
def add(a, b):
    return a + b

# calling function
result_add = add(2, 3)
print("Result of add(2, 3):", result_add)

def add_and_compare(a, b):
    sum_ab = a + b
    if a > b:
        largest = a
    elif b > a:
        largest = b
    else:
        largest = None  # Both numbers are equal
    return sum_ab, largest

# calling function
result_add_and_compare = add_and_compare(2, 3)
print("Result of add_and_compare(2, 3):", result_add_and_compare)