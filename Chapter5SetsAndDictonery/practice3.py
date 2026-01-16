# Create a empty dictionary of your 4 frds and ask them to enter their fav language and store it in the dictionary and print the final dictionary.

fav_languages = {}
for i in range(4):
    name = input("Enter your name: ")
    language = input("Enter your favorite programming language: ")
    fav_languages[name] = language
    
print("Favorite Languages Dictionary:", fav_languages)