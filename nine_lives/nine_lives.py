# Import the random library to randomly select the secret word
import random

# Player starts with 9 lives
lives = 9
# List of possible words for the game
words = ['pizza', 'fairy', 'teeth', 'shirt', 'otter', 'plane']
# Pick a random word from the list to be the secret word
secret_word = random.choice(words)
# Create a clue with '?' showing the length of the secret word
clue = list('?????')
# The heart symbol to represent lives
heart_symbol = u'\u2764'
# A flag to track if the player guessed the word correctly
guessed_word_correctly = False

# This function updates the clue when the player guesses a correct letter
def update_clue(guessed_letter, secret_word, clue):
    index = 0
    # Go through each letter of the secret word
    while index < len(secret_word):
        # If the guessed letter matches a letter in the secret word
        if guessed_letter == secret_word[index]:
            # Update the clue by placing the guessed letter in the correct spot
            clue[index] = guessed_letter
        # Move to the next letter
        index = index + 1

# The game continues as long as the player has lives remaining
while lives > 0:
    # Print the current clue (with correct letters revealed and '?' for hidden letters)
    print(clue)
    # Print how many lives the player has left using heart symbols
    print('Lives left: ' + heart_symbol * lives)
    # Ask the player to guess a letter or the whole word
    guess = input('Guess a letter or the whole word: ')

    # If the player guesses the whole word correctly
    if guess == secret_word:
        guessed_word_correctly = True
        # End the game since they guessed the word
        break

    # If the guessed letter is in the secret word
    if guess in secret_word:
        # Call the function to update the clue with the guessed letter
        update_clue(guess, secret_word, clue)
    else:
        # If the guess is wrong, reduce the player's lives by 1
        print('Incorrect. You lose a life')
        lives = lives - 1
    
# If the player guessed the word correctly, print a winning message
if guessed_word_correctly:
    print('You won! The secret word was ' + secret_word)
# If the player ran out of lives, print a losing message and reveal the word
else:
    print('You lost! The secret word was ' + secret_word)
