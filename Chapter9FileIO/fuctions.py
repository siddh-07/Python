
with open("Chapter9FileIO/file.txt", "r") as file:
    line = file.readline()
    while line != "":
        print(line.strip(),type(line))
        line = file.readline()        
       
with open("Chapter9FileIO/file.txt", "r") as file:      
    lines = file.readlines()
    print(lines,type(lines)) 