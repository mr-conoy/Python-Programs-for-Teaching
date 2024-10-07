# We need to import the 'random' module to select a random word from a list of words.
import random

# This function is the main part of the hangman game. It controls how the game is played.
def hangman():
    # A list of words the player will have to guess from. One word will be chosen randomly each time the game is played.
    words = ["python", "java", "kotlin", "javascript", "ruby"]
    
    # Select a random word from the list of words using 'random.choice'.
    word_to_guess = random.choice(words)
    
    # Create a list of underscores ('_'), the same length as the word to guess. This is what the player will see
    # as they try to guess the letters.
    guessed_word = ["_"] * len(word_to_guess)
    
    # The player starts with 6 attempts. Every time they guess wrong, they lose an attempt.
    attempts_left = 6
    
    # This set will store the letters the player has already guessed to prevent them from guessing the same letter twice.
    guessed_letters = set()
    
    # Print a welcome message when the game starts.
    print("Welcome to Hangman!")
    
    # This 'while' loop runs as long as the player still has attempts left and they haven't guessed the whole word.
    while attempts_left > 0 and "_" in guessed_word:
        # Show the player the current state of the word they're trying to guess, with underscores for the letters they haven't guessed yet.
        print("\nCurrent word: " + " ".join(guessed_word))
        
        # Tell the player how many attempts they have left to guess the word.
        print(f"Attempts left: {attempts_left}")
        
        # Ask the player to guess a letter. 'lower()' makes sure the guess is in lowercase so it matches the word.
        guess = input("Guess a letter: ").lower()
        
        # Check if the player entered something that is not a single letter (like a number or more than one letter).
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")  # Remind them to enter only one letter.
            continue  # Go back to the start of the loop and ask for another guess.
        
        # Check if the player has already guessed this letter before.
        if guess in guessed_letters:
            print("You've already guessed that letter.")  # Let them know they've guessed this one already.
            continue  # Go back to the start of the loop and ask for another guess.
        
        # Add the guessed letter to the set of guessed letters so they don't guess it again.
        guessed_letters.add(guess)
        
        # Check if the guessed letter is in the word to guess.
        if guess in word_to_guess:
            # If the guess is correct, update the guessed word by replacing the corresponding underscores with the guessed letter.
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")  # Tell the player they guessed correctly.
        else:
            # If the guess is wrong, reduce the number of attempts left by 1.
            attempts_left -= 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")  # Let the player know their guess was wrong.
    
    # If the player has guessed the entire word (no underscores left), they win.
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word_to_guess)
    else:
        # If the player has run out of attempts, they lose, and the word is revealed.
        print("\nYou've run out of attempts. The word was:", word_to_guess)

# This checks if the script is being run directly (and not imported from somewhere else),
# and if so, it starts the game by calling the 'hangman' function.
if __name__ == "__main__":
    hangman()
