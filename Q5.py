# def check_divisibility(num, divisor):
#     """
#     Task 1
#     - Create a function to check if the number (num) is divisible by another number (divisor).
#     - Both num and divisor must be numeric.
#     - Return True if num is divisible by divisor, False otherwise.
#     """
#     return


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

#answer
#task 1

def check_divisibility(num, divisor):
    if not isinstance(num, (int, float)) and isinstance(divisor, (int,float)):
        return -1
    else:
        if num % divisor == 0:
            return "Ture"
        else
            return "False"

#task 2
check_divisibility(10, 2)
check_divisibility(7, 3)
