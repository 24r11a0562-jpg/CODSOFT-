import random

user_score = 0
computer_score = 0

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("Final Score")
print("Your Score:", user_score)
print("Computer Score:", computer_score)
print("Thank you for playing!")
output:
Welcome to Rock-Paper-Scissors Game!
Enter rock, paper, or scissors: rock
You chose: rock
Computer chose: scissors
You win!
Your Score: 1
Computer Score: 0
Do you want to play again? (yes/no): no

Final Score
Your Score: 1
Computer Score: 0
Thank you for playing!
