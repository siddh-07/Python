# List Comprehensions

l = [1,2,3,4,5,6,7,8,9,10]

l2 = [x*x for x in l if x%2==0]

print(l2)  # Output: [4, 16, 36, 64, 100]