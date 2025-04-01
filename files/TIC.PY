def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there is a winner."""
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return board[0][i]
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    
    return None

def is_draw(board):
    """Checks if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print_board(board)
    
    while True:
        print(f"Player {current_player}'s turn.")
        try:
            row = int(input("Enter the row (0, 1, 2): "))
            col = int(input("Enter the column (0, 1, 2): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue
        
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        
        board[row][col] = current_player
        print_board(board)
        
        winner = check_winner(board)
        if winner:
            print(f"Player {winner} wins!")
            break
        
        if is_draw(board):
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()