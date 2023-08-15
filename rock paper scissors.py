import random

user_score = 0
computer_score = 0
options = ["rock", "paper", "scissors"]

while True:
    choice = input("Choose Rock/Paper/Scissors or Q to quit: ").lower()
    
    if choice == "q":
        break

    if choice not in options:
        print("Enter a valid choice")
        continue

    random_number = random.randint(0, 2)
    #rock: 0
    #Paper: 1
    #scissors: 2
    computer_choice = options[random_number]

    print(f"Computer picked: {computer_choice}.")

    if choice == "rock" and computer_choice == "scissors":
        print("YOU WON!")
        user_score += 1
        print(f"Your score: {user_score} vs Computer score: {computer_score} ")
    
    elif choice == "paper" and computer_choice == "rock":
        print("YOU WON!")
        user_score += 1
        print(f"Your score: {user_score} vs Computer score: {computer_score} ")
    
    elif choice == "scissors" and computer_choice == "paper":
        print("YOU WON!")
        user_score += 1
        print(f"Your score: {user_score} vs Computer score: {computer_score} ")
    
    else:
        print("YOU LOSE!")
        computer_score += 1
        print(f"Your score: {user_score} vs Computer score: {computer_score} ")


print("Goodbye :)")
