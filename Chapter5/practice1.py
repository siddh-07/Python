# Write a code for dictionary that conatains hindi words and their english translation.

translation = { 
    "Namste": "Hello",
    "Dhanyavad": "Thank you",
    "Ha": "Yes",
    "Na": "No"
}

user_input = input("Enter a Hindi word to translate to English: ")
print("Hindi to English Dictionary:", translation.get(user_input))
