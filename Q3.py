#def update_dictionary(dct, key, value):
#    """
#   Task 1
#    - Create a function that updates a dictionary (dct) with a new key-value pair.
#    - If the key already exists in dct, print the original value, then update its value.
#    - Return the updated dictionary.
#    """
#    return


# Task 2
# Invoke the function "update_dictionary" using the following scenarios:
# - {}, "name", "Alice"
# - {"age": 25}, "age", 26


#answer
#task 1

def update_dictionary(dct, key, value):
    if key in dct:
        dct[key] = value
        print(dct)

#task 2
update_dictionary({}, "name", "alice")
update_dictionary({"age": 25}, "age", 26)
