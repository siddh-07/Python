empty_dictionary = {} # Empty dictionary, not a set
empty_sets = set() # Correct way to create an empty set

empty_sets = {21 ,2, 3,44,5,1,5,5,5} 

print(empty_sets)  # Duplicates are removed and order is not guaranteed

# Methods of sets
set = {1, 2, 3, 4, 5 ,"hello"}

print(type(set))  # <class 'set'>
set.add(6)  # Adding an element to the set
print(set)  # {1, 2, 3, 4, 5, 6, 'hello'}
set.remove(3)  # Removing an element from the set
print(set)  # {1, 2, 4, 5, 6, 'hello'}
# set.pop()  # Removes and returns an arbitrary element from the set
print(set.union(empty_sets)) # Union of two sets, basically it combines both sets
print(set.intersection(empty_sets)) # It gives the common elements in both sets
print({1,2,3}.issubset(set)) # Checks if the set is a subset of another set