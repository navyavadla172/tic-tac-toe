# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if the current player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

# Function to check if the board is full (tie)
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Main function to run the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"  # X always goes first
    
    while True:
        print_board(board)
        
        # Ask for the player's move
        move = input(f"Player {current_player}, enter your move (row col): ").split()
        row, col = int(move[0]), int(move[1])
        
        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This cell is already taken, try again.")
            continue
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check for a tie
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
if __name__ == "__main__":
    play_game()
