import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]


while True:
    user_input = input("Type Rock/ Paper/ Scissors or Q to Quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock is 0, paper is 1, scissors is 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You Won")
        user_wins += 1 
       
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won")
        user_wins += 1 
    elif user_input == "scissors" and computer_pick == "rock":
        print("You Won")
        user_wins += 1 
        
    else:
        print("You Lose")
        computer_wins += 1 
       
print("User", user_wins, " times")
print("Flithy Clanker", computer_wins, " times")
print("goodbye")