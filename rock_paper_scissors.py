import random

print("Welcome to Rock, Paper, Scissors!")
print("Type 'x' to quit.\n")

choices = ["rock", "paper", "scissors"]

while True:
    player = input("Enter rock, paper, or scissors: ").lower()

    if player == "x":
        print("Game over. Thanks for playing!")
        break

    if player not in choices:
        print("Invalid choice! Please type rock, paper, or scissors.")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") \
         or (player == "paper" and computer == "rock") \
         or (player == "scissors" and computer == "paper"):
        print("You win! 🏆")
    else:
        print("You lose! 😞")
