import random

def dice_rolling_game():
    print("Welcome to the Dice Rolling Game!")
    
    while True:
        roll = input("Press Enter to roll the dice (or type 'quit' to exit): ")
        
        if roll.lower() == "quit":
            print("Thanks for playing!")
            break
        
        dice_roll = random.randint(1, 6)
        print(f"You rolled a {dice_roll}!")
        
        if dice_roll == 6:
            print("You win!")
        else:
            print("Try again!")
            
if __name__ == "__main__":
    dice_rolling_game()
