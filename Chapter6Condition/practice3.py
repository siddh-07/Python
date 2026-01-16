
# This program checks if a user comment is spam based on certain phrases.
comment = str(input("Enter a comment: "))

if (comment.__contains__("Make a lot of money") or 
    comment.__contains__("Buy now") or 
    comment.__contains__("Subscribe this") or 
    comment.__contains__("Click this")):
    print("This comment is spam.")
else:
    print("This comment is not spam.")

# Alternatively, using 'in' operator for better readability
if ("Make a lot of money" in comment or 
    "Buy now" in comment or 
    "Subscribe this" in comment or 
    "Click this" in comment):
    print("This comment is spam.")
else:
    print("This comment is not spam.")
    