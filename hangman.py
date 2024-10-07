import random

def hangman():
    words = ["python", "java", "kotlin", "javascript", "ruby"]
    word_to_guess = random.choice(words)
    guessed_word = ["_"] * len(word_to_guess)
    attempts_left = 6
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    
    while attempts_left > 0 and "_" in guessed_word:
        print("\nCurrent word: " + " ".join(guessed_word))
        print(f"Attempts left: {attempts_left}")
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            for i, letter in enumerate(word_to_guess):
                if letter == guess:
                    guessed_word[i] = guess
            print("Good guess!")
        else:
            attempts_left -= 1
            print(f"Incorrect! The letter '{guess}' is not in the word.")
    
    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:", word_to_guess)
    else:
        print("\nYou've run out of attempts. The word was:", word_to_guess)

if __name__ == "__main__":
    hangman()
