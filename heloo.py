board =[" " for _ in range(9)]

def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)            # diagonals
]
    for a,b,c in winning_positions:
     if board[a] == player and board[b] == player and board[c] == player:
         return True
    return False
    # Game starts 
current_player = "X"

print("Welcome to Tic Tac Toe!")
print("Player 1 is X and Player 2 is O.")
print("Enter a number between 1 and 9 to place your mark.")

while True:
    display_board()

    try:
        position = int(input(f"Player {current_player}, choose your position (1-9): "))


        if position < 1 or position > 9:
            print(" Please choose a number between 1 and 9.")
            continue

        index = position - 1
        if board[index] != " ":
            print("Position already taken. Choose another position.")
            continue

        board[index] = current_player

        if check_winner(current_player):
            display_board()
            print(f"Player {current_player} wins!")
            break

        if " " not in board:
            display_board()
            print("It's a draw!")
            break
             
        current_player = "O" if current_player == "X" else "X"

    except ValueError:

        print(" Please enter a number between 1 and 9.")
                