# Example of Map
numbers = [1, 2, 3, 4, 5]
squres = lambda x: x * x

squared_numbers = list(map(squres, numbers))

print("Squared Numbers using map:", squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Example of Filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
is_even = lambda x: x % 2 == 0
even_numbers = list(filter(is_even, numbers))
print("Even Numbers using filter:", even_numbers)  # Output: [2, 4, 6, 8, 10]

# Example of Reduce
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_numbers = lambda x, y: x + y
total = reduce(sum_numbers, numbers)
print("Sum of Numbers using reduce:", total)  # Output: 15