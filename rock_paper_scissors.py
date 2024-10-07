# We need to import the 'random' module to allow the computer to randomly choose between rock, paper, or scissors.
import random

# This function is the main part of the Rock, Paper, Scissors game.
def rock_paper_scissors():
    
    # Print a welcome message to the player when the game starts.
    print("Welcome to Rock, Paper, Scissors!")
    
    # Create a list of the three possible choices in the game: rock, paper, and scissors.
    choices = ["rock", "paper", "scissors"]
    
    # This 'while' loop will keep the game going until the player decides to quit.
    while True:
        # Ask the player to choose rock, paper, or scissors (or type 'quit' to exit the game). The input is converted to lowercase to match the choices.
        player_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        
        # If the player types 'quit', the game will end with a 'Thanks for playing!' message.
        if player_choice == "quit":
            print("Thanks for playing!")
            break  # 'break' stops the loop and ends the game.
        
        # Check if the player's choice is not one of the valid options (rock, paper, or scissors).
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")  # Ask them to choose correctly.
            continue  # 'continue' makes the loop repeat and ask for another choice.
        
        # The computer randomly selects rock, paper, or scissors using 'random.choice' from the list of choices.
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")  # Show the player what the computer chose.
        
        # If the player's choice is the same as the computer's choice, it's a tie.
        if player_choice == computer_choice:
            print("It's a tie!")  # Inform the player that both made the same choice.
        
        # The player wins if they choose rock and the computer chooses scissors,
        # or if they choose paper and the computer chooses rock,
        # or if they choose scissors and the computer chooses paper.
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")  # Let the player know they've won the round.
        
        # If none of the above conditions are met, the player loses.
        else:
            print("You lose!")  # Tell the player that they lost the round.

# This checks if the script is being run directly (and not imported from somewhere else),
# and if so, it starts the game by calling the 'rock_paper_scissors' function.
if __name__ == "__main__":
    rock_paper_scissors()
