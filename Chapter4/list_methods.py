friends = ["Siddh","Harry",1,True,5.6,"Ron"]
# Before using list methods
print("Original List:",friends)

# Unlike strings list modification methods do not return a new list, they modify the existing list and return None.
friends.append("Hermione")  # Adds "Hermione" to the end of the list
print("Append Method:",friends)

numbers = [3, 5, 2, 8, 6, 1]
print("Original List:",numbers)
numbers.sort()  # Sorts the list in ascending order
print("List sort:",numbers)
numbers.reverse()  # Reverses the order of the list
print("Reverse List:",numbers)
numbers.insert(2, 4)  # Inserts 4 at index 2
print("Insert number at certain Index:",numbers)
numbers.remove(5)  # Removes the first occurrence of 5
print("Remove number '5' from list:",numbers)
numbers.pop(2)  # Removes the element at index 2
print("Remove number from index 2:",numbers)