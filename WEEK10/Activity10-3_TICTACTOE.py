def create_board(): #Create a list 3x3 Grid
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def display_board(board): #Print Visual Rep and format into 3x3 Grid w/ dividing lines
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

#Player Move - with the valid range 1-9
def make_move(board, position, player):
    if position < 1 or position > 9:
        return False
    if board[position-1] in ['X', 'O']:
        return False
    board[position-1] = player
    return True


# Check Winner
def check_winner(board):
    wins = [                              # Winning combinations
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(board[a] == board[b] == board[c] for a, b, c in wins)

# Main Game
def play_game():
    board = create_board()
    player = 'X'
    print("Welcome to Tic-tac-toe!")
    print("Enter a number (1-9) to make your move:")
    
    for _ in range(9):
        display_board(board)
        print(f"Player {player}'s turn")
        
        while True:
            try:
                position = int(input("Enter position (1-9): "))
                if make_move(board, position, player):
                    break
                print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number between 1-9!")
        
        if check_winner(board):
            display_board(board)
            print(f"Player {player} wins!")
            return
        
        player = 'O' if player == 'X' else 'X'    
    display_board(board)
    print("It's a tie!")


# Start the game
if __name__ == "__main__":
    play_game()

