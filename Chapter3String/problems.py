# Write a program to display use enter name followed by good morning

name = input("Enter your name: ")

print("Good morning, " + name + "!")
# Alternatively, using f-string for formatted output
print(f"Good morning, {name}!") 

# Write a program which fil name and date in this letter

letter = "Dear <|NAME|>\nDate: <|DATE|>,\n\tYou are selected!"
date = input("Enter the date: ")

print(letter.replace("<|NAME|>", name).replace("<|DATE|>", date))

# Write a program to detect double spaces in a string
string_with_double_spaces = "This  is a string with double spaces."
double_space_index = string_with_double_spaces.find("  ")
if double_space_index != -1:
    print(f"Double spaces found at index: {double_space_index}")
    #Replace with single space
    print("String after replacing double spaces with single space:",string_with_double_spaces.replace("  ", " "))
else:
    print("No double spaces found.")
    
# Write a program to format the following letter using escape sequence characters
letter_format = "Dear Friend,\n\tI hope you are doing well.\n\tLet's catch up sometime soon.\nBest Regards,\nYour Name"

print(letter_format)