# Importing the random module to allow the computer to make random choices
import random 

# Initialize counters for user wins, computer wins, ties, and total rounds played
user_wins = 0
computer_wins = 0
tie = 0
total_rounds = 0

# Define the possible options for the game in list
options = ["rock", 'paper', 'scissors']

# Start the game loop
while True:
    # Get input from the user
    user_input = input("Type Rock/Paper/Scissor or Q to quti: ").lower()

    # If the user wants to quit, break out of the loop
    if user_input == "q":
        break

    # If the input is not valid, skip this iteration and ask again
    if user_input not in options:
        continue

    # Increment the total rounds counter
    total_rounds += 1  

    random_number = random.randint(0,2)
    # rock: 0, paper: 1, scissors: 2

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    # Determine the winner for each possible outcome
    if user_input == "rock" and computer_pick == "scissors" :
        print("You Won!")
        user_wins += 1
        continue

    elif user_input == "rock" and computer_pick == "paper" :
        print("Computer Won!")
        computer_wins += 1

    elif user_input == "paper" and computer_pick == "rock" :
        print("You Won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "scissors" :
        print("Computer Won!")
        computer_wins += 1    

    elif user_input == "scissors" and computer_pick == "paper":
        print("You Won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "rock":
        print("Computer Won!")
        computer_wins += 1   

    else:
        user_input == computer_pick 
        print("Tie!")
        tie += 1    

# Print final results after exiting the loop        
print("You Won", user_wins, "times.")
print("The Computer Won", computer_wins, "times.")
print("Tie", tie, "times.")
print("Total Number of Rounds", total_rounds, "rounds.")
print("Good Bye!!")
