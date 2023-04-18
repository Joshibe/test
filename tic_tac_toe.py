# board, display board, play game
# handle turn, check win, check row, check diagonal
# check tie, flip player
# Global Variables
game_progress = True

# Who won? Or tie?
winner = None

# Who turn is next
current_player = "X"

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic-tac-toe
def play_game():
    # Display the initial board
    display_board()
    # While the game is in progress
    while game_progress:
        # Handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip to the other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn of an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in["1","2","3","4","5","6","7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go again")

        board[position] = player

        display_board()


# Check if game is over
def check_if_game_over():
    check_for_winner()
    check_if_tie()


# Check for a winner
def check_for_winner():
    global winner
    # check row
    row_winner = check_rows()
    # check column
    column_winner = check_columns()
    # check diagonal
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        # there was no win
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_progress
    # Check if any of the row have all the same value(and is not equal)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_progress = False
    # Return the Winner "X" or "O"
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_progress
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_progress = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    global game_progress
    diag_1 = board[0] == board[4] == board[8] != "-"
    diag_2 = board[6] == board[4] == board[2] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diag_1 or diag_2:
        game_progress = False
    if diag_1:
        return board[0]
    elif diag_2:
        return board[6]
    return


def check_if_tie():
    global game_progress
    if "-" not in board:
        game_progress = False
    return


def flip_player():
    # Global variable we need
    global current_player
    # If the current player was X, change it to O
    if current_player == "X":
        current_player = "O"
    # If the current player was O, change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
