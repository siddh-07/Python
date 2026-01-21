# This script demonstrates basic exception handling in Python.
# This can prevent the program from crashing due to unexpected errors. 
try:
    number = int(input("Enter a number: "))
    print(f"You entered: {number}")
    
# Catch any exception that occurs in the try block
# For Specific exceptions, you can replace 'Exception' with the specific exception type like ValueError, TypeError, etc.
except Exception as e: 
    print(f"An error occurred: {e}")
else:
    print("No errors occurred.") # This block runs if no exceptions were raised in the try block.
    
finally:
    print("Execution completed.") # This block always runs, regardless of whether an exception occurred or not.