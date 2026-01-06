# What is Tuple 
# A tuple is a collection which is ordered and unchangeable. In Python, tuples are written with round brackets.

numers = (1, 2, 3, 4, 5) # This is not a list or string, this is a tuple
print(type(numers)) # Output: <class 'tuple'>

#how to create empty tuple
empty_tuple = ()
print(type(empty_tuple)) # Output: <class 'tuple'>

#How to create a tuple with single element
number = (1) # this is not a tuple, this is an integer
single_element_tuple = (5,) # Note the comma
print(type(single_element_tuple),type(number)) 