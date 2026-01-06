# Methods for Tuples in Python  
# Tuples have only two built-in methods: count() and index().

numbers = (1, 2, 3.5, False,"Hello") # Creating a tuple with different data types
print("Original Tuple:",numbers)

# count() method
print("Count of 2 in tuple:",numbers.count(2)) # Output: 1
print("Count of 10 in tuple:",numbers.count(10)) # Output: 0

# index() method
# The index() method raises a ValueError if the value is not found
print("Index of 3.5 in tuple:",numbers.index(3.5)) # Output: 2
print("Index of False in tuple:",numbers.index(False)) # Output: 3
