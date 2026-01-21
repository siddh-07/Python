from random import randint

random_number = randint(1, 100)
number = int(input("Guess a number between 1 and 100: "))

guesses = 0 
while (number != random_number):
    guesses += 1
    if number < random_number:
        print("Guess higher number!")
    else:
        print("guess lower number!")
        
    number = int(input("Guess again: "))
    
print(f"Congratulations! You guessed the number {random_number} in {guesses} gusses.")

    
      