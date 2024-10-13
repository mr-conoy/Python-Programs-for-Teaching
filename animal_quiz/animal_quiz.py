# This function checks if the player's guess is correct
def check_guess(guess, answer):
    # We need to update the global score, so we use 'global' to access it
    global score
    # still_guessing helps keep track if the player is still guessing
    still_guessing = True
    # This is the number of attempts the player has made
    attempt = 0
    # While the player is still guessing and has fewer than 3 attempts
    while still_guessing and attempt < 3:
        # Check if the guess (converted to lowercase) matches the correct answer
        if guess.lower() == answer.lower():
            # If it's correct, tell the player and increase the score by 1
            print("Correct Answer")
            score = score + 1
            # Stop guessing since they got it right
            still_guessing = False
        else:
            # If the guess is wrong and there are still attempts left
            if attempt < 2:
                # Ask the player to try again
                guess = input("Sorry wrong answer. Try again. ")
            # Increase the attempt count by 1
            attempt = attempt + 1
    
    # If the player has used all 3 attempts, show the correct answer
    if attempt == 3:
        print("The correct answer is ", answer)

# Initialize the player's score to 0 at the start of the game
score = 0
print("Guess the Animal")

# Ask the player to guess which bear lives at the North Pole
guess1 = input("Which bear lives at the North Pole? ")
# Call the check_guess function to see if their answer is "polar bear"
check_guess(guess1, "polar bear")

# Ask the player to guess which is the fastest land animal
guess2 = input("Which is the fastest land animal? ")
# Check if their answer is "cheetah"
check_guess(guess2, "cheetah")

# Ask the player to guess which is the largest animal
guess3 = input("Which is the largest animal? ")
# Check if their answer is "blue whale"
check_guess(guess3, "blue whale")

# After all the questions, show the player's final score
print("Your Score is " + str(score))
