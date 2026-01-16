# Methods of Dictionaries in Python

marks = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Siddh" : 99,
}

print( marks.values()) # Returns a view object of all values in the dictionary
print( marks.keys()) # Returns a view object of all keys in the dictionary
print( marks.items()) # Returns a view object of all key-value pairs in the dictionary
print( marks.get("Alice")) # Returns the value for the specified key ("Alice")
print(marks.get("Devid")) # Returns None since "David" key doesn't exist in the dictionary
print(marks["Alice"]) #  Returns the value for the specified key ("Alice")
# print(marks["Devid"]) # Raises KeyError since "David" key doesn't exist in the dictionary
marks.update({"David":88 ,"Siddh":100})  # Update the value of existing key and Adds a new key-value pair ("David": 88) to the dictionary if its not already present
print("Updated Marks Dictionary:", marks)