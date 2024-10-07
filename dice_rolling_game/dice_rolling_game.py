# We need to import the 'random' module to generate random numbers, 
# which we will use to simulate the rolling of a dice.
import random

# This function is the main part of the game. It controls everything that happens when the game runs.
def dice_rolling_game():
    
    # This prints a welcome message to the player when the game starts.
    print("Welcome to the Dice Rolling Game!")
    
    # This 'while' loop keeps the game going until the player decides to stop.
    while True:
        # The input function waits for the player to press Enter or type 'quit' to stop the game.
        roll = input("Press Enter to roll the dice (or type 'quit' to exit): ")
        
        # This checks if the player typed 'quit' (in any combination of uppercase or lowercase letters).
        # If they did, the game ends, and a 'Thanks for playing!' message is shown.
        if roll.lower() == "quit":
            print("Thanks for playing!")
            break  # 'break' stops the loop and ends the game.
        
        # This line generates a random number between 1 and 6, just like rolling a dice.
        dice_roll = random.randint(1, 6)
        
        # This prints out the result of the dice roll, telling the player what number they rolled.
        print(f"You rolled a {dice_roll}!")
        
        # If the player rolls a 6, they win the game.
        if dice_roll == 6:
            print("You win!")  # This message is shown when the player wins.
        else:
            # If the player doesn't roll a 6, they're encouraged to try again.
            print("Try again!")

# This checks if the script is being run directly (and not imported from somewhere else),
# and if so, it starts the game by calling the 'dice_rolling_game' function.
if __name__ == "__main__":
    dice_rolling_game()
