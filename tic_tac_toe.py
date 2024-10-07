def print_board(board):
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_winner(board, player):
    win_conditions = [
        [(0, 0), (0, 1), (0, 2)],  # top row
        [(1, 0), (1, 1), (1, 2)],  # middle row
        [(2, 0), (2, 1), (2, 2)],  # bottom row
        [(0, 0), (1, 0), (2, 0)],  # left column
        [(0, 1), (1, 1), (2, 1)],  # middle column
        [(0, 2), (1, 2), (2, 2)],  # right column
        [(0, 0), (1, 1), (2, 2)],  # diagonal
        [(0, 2), (1, 1), (2, 0)]   # diagonal
    ]
    
    for condition in win_conditions:
        if all([board[x][y] == player for x, y in condition]):
            return True
    return False

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0
    moves = 0
    
    print("Welcome to Tic-Tac-Toe!")
    
    while moves < 9:
        print_board(board)
        print(f"Player {players[current_player]}'s turn.")
        
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = players[current_player]
            moves += 1
            
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                return
            
            current_player = 1 - current_player
        else:
            print("That spot is already taken. Try again.")
    
    print_board(board)
    print("It's a tie!")

if __name__ == "__main__":
    tic_tac_toe()
