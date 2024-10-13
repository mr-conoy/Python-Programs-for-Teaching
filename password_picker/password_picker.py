# We are going to use random choices to create passwords, so we need the random and string libraries
import random
import string

# List of descriptive words (adjectives) to choose from for the password
adjectives = ['sleepy', 'slow', 'smelly',
                'wet', 'fat', 'red',
                'orange', 'yellow', 'green',
                'blue', 'purple', 'fluffy',
                'white', 'proud', 'brave']

# List of objects or things (nouns) to choose from for the password
nouns = ['apple', 'dinosaur', 'ball',
        'toaster', 'goat', 'dragon',
        'hammer', 'duck', 'panda']

# Print a message to welcome the user to the password generator
print("Welcome to Password Picker!")

# We want to keep generating passwords until the user decides to stop
while True:
    # Pick a random adjective from the list
    adjective = random.choice(adjectives)
    # Pick a random noun from the list
    noun = random.choice(nouns)
    # Pick a random number between 0 and 99
    number = random.randrange(0, 100)
    # Pick a random special character like @, !, # from the string.punctuation set
    special_char = random.choice(string.punctuation)

    # Combine all parts to form the password: adjective + noun + number + special character
    password = adjective + noun + str(number) + special_char
    # Print out the generated password for the user
    print("Your new password is: %s" % password)

    # Ask the user if they want another password
    response = input("Would you like another password? Type y or n: ")
    # If the user types 'n', stop the loop and end the program
    if response == 'n':
        break
