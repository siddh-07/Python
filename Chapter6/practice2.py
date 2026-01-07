# Write a program to take marks of 3 subjects from the user and calculate the total percentage.

math = int(input("Enter your Math marks: "))
science = int(input("Enter your Science marks: "))
english = int(input("Enter your English marks: "))

total_percentage = int((math + science + english) / 3)
print("Total Percentage:", total_percentage)

if (total_percentage >=40) and (math >=33) and (science >=33) and (english >=33):
    print("Congratulations! You have passed the exam.")
else:
    print("Sorry, you have failed the exam.")
    
    