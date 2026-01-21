
name: str = "Siddh Bhadani"
def get_name() -> str:
    return name

name = get_name()
print(f"My name is {name}")

name : str = int(1) # type hinting with variable annotation this is just a hint not a type cast

print(f"My name is {name}")
