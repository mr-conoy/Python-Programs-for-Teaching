# This function prints the current state of the Tic-Tac-Toe board.
# It formats each row of the board, separating the cells with a "|".
def print_board(board):
    # "\n".join joins each row of the board into a string with newlines in between, making it look like a grid.
    print("\n".join([" | ".join(row) for row in board]))
    print()  # Prints an empty line for better readability.

# This function checks if a player has won the game by matching their marks (X or O) to one of the winning conditions.
def check_winner(board, player):
    # These are all the possible winning conditions for Tic-Tac-Toe:
    # 3 marks in a row (horizontally), column (vertically), or diagonally.
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # top row
        [(1, 0), (1, 1), (1, 2)],  # middle row
        [(2, 0), (2, 1), (2, 2)],  # bottom row
        [(0, 0), (1, 0), (2, 0)],  # left column
        [(0, 1), (1, 1), (2, 1)],  # middle column
        [(0, 2), (1, 2), (2, 2)],  # right column
        [(0, 0), (1, 1), (2, 2)],  # diagonal from top-left to bottom-right
        [(0, 2), (1, 1), (2, 0)]   # diagonal from top-right to bottom-left
    ]
    
    # Loop through each winning condition to check if the player has marked all the spots in that condition.
    for condition in win_conditions:
        # If all positions in a winning condition match the player's mark (X or O), return True (the player has won).
        if all([board[x][y] == player for x, y in condition]):
            return True
    # If none of the winning conditions are met, return False (no winner yet).
    return False

# This function contains the main game loop for Tic-Tac-Toe.
def tic_tac_toe():
    # Initialize an empty 3x3 board, where each cell is a space (" ") to represent an unoccupied spot.
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    # Players are represented as "X" and "O".
    players = ["X", "O"]
    
    # current_player keeps track of which player's turn it is (0 for X, 1 for O).
    current_player = 0
    
    # moves counts how many turns have been played. A game can have a maximum of 9 moves (since the board has 9 spots).
    moves = 0
    
    # Print a welcome message when the game starts.
    print("Welcome to Tic-Tac-Toe!")
    
    # This loop continues until all 9 moves are made, or a player wins.
    while moves < 9:
        # Display the current state of the board.
        print_board(board)
        
        # Inform the current player (X or O) that it's their turn.
        print(f"Player {players[current_player]}'s turn.")
        
        # Ask the player to input the row (0, 1, or 2) they want to mark.
        row = int(input("Enter row (0-2): "))
        
        # Ask the player to input the column (0, 1, or 2) they want to mark.
        col = int(input("Enter column (0-2): "))
        
        # Check if the selected spot is empty (i.e., contains a space " ").
        if board[row][col] == " ":
            # If the spot is empty, mark it with the current player's symbol (X or O).
            board[row][col] = players[current_player]
            
            # Increment the move counter, as a valid move has been made.
            moves += 1
            
            # Check if the current player has won the game after this move.
            if check_winner(board, players[current_player]):
                # If they have won, print the board and display a winning message.
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                return  # End the game.
            
            # Switch to the other player by changing current_player (0 to 1 or 1 to 0).
            current_player = 1 - current_player
        else:
            # If the spot is already taken, inform the player and let them try again.
            print("That spot is already taken. Try again.")
    
    # If the loop finishes without a winner, it means all 9 moves have been made and

