# Write a Python program to find the greatest of four numbers entered by the user.

l1 = []

l1.append(input("Enter First number: "))
l1.append(input("Enter Second number: "))
l1.append(input("Enter Third number: "))
l1.append(input("Enter Fourth number: "))

if (l1[0] >= l1[1]) and (l1[0] >= l1[2]) and (l1[0] >= l1[3]):
    print("First number is the greatest:", l1[0])
elif (l1[1] >= l1[0]) and (l1[1] >= l1[2]) and (l1[1] >= l1[3]):
    print("Second number is the greatest:", l1[1])
elif (l1[2] >= l1[0]) and (l1[2] >= l1[1]) and (l1[2] >= l1[3]):
    print("Third number is the greatest:", l1[2])
else:
    print("Fourth number is the greatest:", l1[3])            