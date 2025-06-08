#simple CLI code for tic tac toe game

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # main diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # anti-diagonal
        return True
    return False

def is_full(board):
    return all([cell in ["X", "O"] for row in board for cell in row])

# Initialize 3x3 board
board = [["1", "2", "3"],
         ["4", "5", "6"],
         ["7", "8", "9"]]

current_player = "X"

while True:
    print_board(board)
    move = input(f"Player {current_player}, enter a number (1-9): ")

    if not move.isdigit() or not (1 <= int(move) <= 9):
        print("Invalid move. Try again.")
        continue

    move = int(move) - 1
    row, col = move // 3, move % 3

    if board[row][col] in ["X", "O"]:
        print("That spot is already taken. Try again.")
        continue

    board[row][col] = current_player

    if check_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break

    if is_full(board):
        print_board(board)
        print("It's a tie!")
        break

    current_player = "O" if current_player == "X" else "X"
