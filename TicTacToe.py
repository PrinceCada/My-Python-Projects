# ---------- Global Variables ----------

# Design of the board
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


# If the game is still going
game_still_going = True


# Who won? or Tie?
winner = None


# Whose turn is it
current_player = "X"


def display_board():
    print("|" + board[0] + "|" + board[1] + "|" + board[2] + "|")
    print("|" + board[3] + "|" + board[4] + "|" + board[5] + "|")
    print("|" + board[6] + "|" + board[7] + "|" + board[8] + "|")


# Play a game Tic Tac Toe
def play_game():

    # display initial board
    display_board()

    # While the game is still on going
    while game_still_going:

        # Handle a single turn
        handle_turn(current_player)

        # Check if the game is over
        check_if_game_over()

        # Flip to other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " WON ")

    elif winner == None:
        print("It's a TIE")


# Handle a single turn
def handle_turn(player):

    # Show whose the next player/turn
    print(player + "'s turn.")
    position = input("Choose a position from 1 - 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1 - 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Try another position")

    board[position] = player

    display_board()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():

    # Setup global variables
    global winner

    # Check rows
    row_winner = check_rows()

    # Check columns
    column_winner = check_column()

    # Check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner

    elif column_winner:
        winner = column_winner

    elif diagonal_winner:
        winner = diagonal_winner

    else:
        winner = None

    return


def check_rows():
    # Setup global variables
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, flag that there is a winner
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_column():
    # Setup global variables
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any row does have a match, flag that there is a winner
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Setup global variables
    global game_still_going

    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    # If any row does have a match, flag that there is a winner
    if diagonals_1 or diagonals_2:
        game_still_going = False

    # Return winner X or O
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return


def check_if_tie():
    # Setup global variable
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return


def flip_player():
    # Setup global variables
    global current_player

    # If the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    # If the current player was o, then change it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
