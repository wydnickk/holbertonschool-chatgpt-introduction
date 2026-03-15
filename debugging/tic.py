#!/usr/bin/python3

def print_board(board):
    """Print the current tic-tac-toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 9)

def check_winner(board):
    """Return 'X' or 'O' if there is a winner, otherwise return None."""
    # rows
    for row in board:
        if row[0] != " " and row.count(row[0]) == len(row):
            return row[0]

    # columns
    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]

    # diagonals
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]

    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    return None

def is_draw(board):
    """Return True if the board is full and there is no winner."""
    return all(cell != " " for row in board for cell in row)

def prompt_int(message, valid_values):
    """
    Ask the user for an integer until they enter a valid one.

    message: prompt text
    valid_values: a set/list of allowed ints (e.g. {0,1,2})
    """
    while True:
        raw = input(message).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Invalid input. Please enter a number (0, 1, or 2).")
            continue

        if value not in valid_values:
            print("Out of range. Please enter 0, 1, or 2.")
            continue

        return value

def tic_tac_toe():
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # stop conditions
        winner = check_winner(board)
        if winner is not None:
            print("Player " + winner + " wins!")
            break
        if is_draw(board):
            print("It's a draw!")
            break

        row = prompt_int("Enter row (0, 1, or 2) for player " + player + ": ", {0, 1, 2})
        col = prompt_int("Enter column (0, 1, or 2) for player " + player + ": ", {0, 1, 2})

        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        board[row][col] = player
        player = "O" if player == "X" else "X"

    # final board
    print_board(board)

if __name__ == "__main__":
    tic_tac_toe()
