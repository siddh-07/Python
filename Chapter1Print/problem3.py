import os

directory_path = '/Users/siddhbhadani/Documents/GitHub'

# Get the list of files and directories in the specified path
contets = os.listdir(directory_path)

# Print the contents of the directory
for item in contets:
    print(item)
