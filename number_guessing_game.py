# We need to import the 'random' module to generate a random number for the player to guess.
import random

# This function is the main part of the number guessing game.
def number_guessing_game():
    
    # Print a welcome message to the player when the game starts.
    print("Welcome to the Number Guessing Game!")
    
    # Let the player know that the secret number will be between 1 and 100.
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100 using 'random.randint'.
    secret_number = random.randint(1, 100)
    
    # This variable keeps track of how many attempts the player has made.
    attempts = 0
    
    # This 'while' loop runs until the player guesses the correct number.
    while True:
        # Ask the player to enter their guess.
        guess = input("Enter your guess: ")
        
        # Check if the player has entered a valid number (digits only). 
        # If they haven't, tell them and go back to the start of the loop.
        if not guess.isdigit():
            print("Please enter a valid number.")  # This message shows if the player doesn't enter a number.
            continue  # 'continue' makes the loop repeat and ask for another guess.
        
        # Convert the player's guess from a string to an integer (a whole number).
        guess = int(guess)
        
        # Increase the attempt count by 1, since the player made a guess.
        attempts += 1
        
        # Check if the player's guess is lower than the secret number.
        if guess < secret_number:
            print("Too low!")  # Tell the player their guess was too low.
        # Check if the player's guess is higher than the secret number.
        elif guess > secret_number:
            print("Too high!")  # Tell the player their guess was too high.
        # If the guess is not lower or higher, it must be correct!
        else:
            # Congratulate the player and tell them how many attempts it took to guess the number.
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break  # 'break' ends the loop because the player has won the game.

# This checks if the script is being run directly (and
