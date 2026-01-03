
name = "Siddh"

# Index 0 will be included, index 3 will be excluded
short_name = name[0:3] # Starting from index 0 to index 3 (not inclusive)

print("Full Name:",name)        # Output: Siddh
print("Short Name:",short_name)  # Output: Sid

# Negative indexing

last_char = name[-1]  # Accessing the last character using negative indexing
short_name = name[-5:-2]  # Accessing characters from index -5 to -2 (not inclusive)
print("Last Character:", last_char)  # Output: h
print("Short Name using negative indexing:", short_name)  # Output: Sid