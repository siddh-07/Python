
file = open("Chapter9FileIO/file.txt", "r")
file_contents = file.read()
print(file_contents)
file.close()

# Alternatively, using 'with' statement to handle file closing automatically
with open("Chapter9FileIO/file.txt", "r") as file:
    file_contents = file.read()
    print(file_contents)
