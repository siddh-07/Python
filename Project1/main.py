# Create a Stone Paper Scissors game
import random
computer = random.choice(['stone', 'paper', 'scissors'])
user = input("Enter your choice (stone, paper, scissors): ").lower()

if user == computer:
    print(f"Both chose {user}. It's a tie!")
elif (user == 'stone' and computer == 'scissors') or (user == 'paper' and computer == 'stone') or (user == 'scissors' and computer == 'paper'):
        print(f"You chose {user} and the computer chose {computer}. You win!")
else:
    print(f"You chose {user} and the computer chose {computer}. You lose!")
        