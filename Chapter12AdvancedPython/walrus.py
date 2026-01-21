# This code demonstrates the use of the walrus operator (:=) in Python
# to assign values to variables as part of an expression.

if (n := len([1, 2, 3, 4, 5])) > 2: 
    print(f"The list is too long with {n} elements.")