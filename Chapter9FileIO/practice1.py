
with open("Chapter9FileIO/poem.txt", "r") as file:      
    lines = file.readlines()
    for line in lines:
        print(line.strip())
        lower = line.lower()
        if "twinkle" in lower:
            print("Found 'twinkle' in line:", line.strip())
            
            