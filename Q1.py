#def swap(x, y):
    """
    Task 1
    - Create a function that would swap the value of x and y using only x and y as variables.
    - x and y must be numeric.
    - Return -1 if x and y is not numeric, and
    - print the swapped values if both x and y are numeric.
    """
    return
  

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

# answer the question
# task 1

def swap(x, y):
    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return -1
    else: 
        x, y = y, x
        print(f"{x}, {y}")
# task 2
swap("apple", 10)
swap(9, 17)
