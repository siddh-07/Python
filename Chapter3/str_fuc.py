# String functions and methods in Python

name = "sIdDh Bhadani"

print("Original Name:", name)
# Length of the string
print("\nLength of Name:", len(name)) 
# endswith() method
print("\nDoes the name end with 'dh'?", name.endswith("dh")) 
# startswith() method
print("\nDoes the name start with 'Si'?", name.startswith("Si")) # Case-sensitive
# capitalize() method
print("\nCapitalized Name:", name.capitalize()) # Capitalizes the first letter
# upper() method
print("\nUppercase Name:", name.upper()) # Converts to uppercase
# lower() method
print("\nLowercase Name:", name.lower()) # Converts to lowercase
# title() method
print("\nTitle Case Name:", name.title()) # Converts to every first letter of each word to uppercase
# find() method
print("\nIndex of 'Bhadani':", name.find("Bhadani")) # Returns the starting index of the substring
# replace() method
print("\nReplaced Name:", name.replace("Bhadani", "Smith")) # Replaces substring with another substring