# _______global variable_____________


# board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True

# who won? or tie?
winner = None

# who's turn is it?
current_player = "X"


def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display the board
    display()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("tie.")


def handle_turn(current_player):

    print(current_player+"'s turn.")
    position = input("choose a position from 1 to 9: ")

    valid=False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position=input("Invalid input! choose a position from 1 to 9: \n")

        position = int(position) - 1

        if board[position]=="-":
            valid=True
        else:
            print("You can't go there. Go again!")

    board[position] =current_player
    display()


def check_if_game_over():
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner
    # check rows
    rows_winner=check_rows()
    # check columns
    columns_winner=check_columns()
    # check diagonals
    diagonals_winner=check_diagonals()

    if rows_winner:
        winner=rows_winner
    elif columns_winner:
        winner=columns_winner
    elif diagonals_winner:
        winner=diagonals_winner
    else:
        winner=None
    return

def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going=False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global  game_still_going
    columns_1 = board[0] == board[3] == board[6] != "-"
    columns_2 = board[1] == board[4] == board[7] != "-"
    columns_3 = board[2] == board[5] == board[8] != "-"

    if columns_1 or columns_2 or columns_3:
        game_still_going = False

    if columns_1:
        return board[0]
    elif columns_2:
        return board[1]
    elif columns_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"

    if diagonals_1 or diagonals_2:
        game_still_going=False

    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return

def check_if_tie():
    return


def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return


play_game()