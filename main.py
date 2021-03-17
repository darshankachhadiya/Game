# board
# display board
# play game
# check win
# check raw
# check columns
# check diagonals
# check tie
# flip player

# ----global variable-----

board = ["-" , "-" , "-" ,
         "-" , "-" , "-" ,
         "-" , "-" , "-" , ]
game_still_going = True

# who won? or Tie?
winner = None

# whose turn is it
current_player = "X"


def play_game():
    display_board ( )

    # call function
    # display initial board
    # while the game is still going
    while game_still_going:
        # handle a single turn of a player
        handle_turn ( current_player )

        # check if the  game is ended
        check_if_game_over ( )

        # flip to the other player
        flip_player ( )

    # the game has ended
    if winner == "X" or winner == "O":
        print ( winner + "won." )
    elif winner == None:
        print ( "Tie." )


def display_board():
    print ( "\n" )
    print ( board[0] + " | " + board[1] + " | " + board[2] )
    print ( board[3] + " | " + board[4] + " | " + board[5] )
    print ( board[6] + " | " + board[7] + " | " + board[8] )
    print ( "\n" )


# handle a single turn of a player
def handle_turn(player):
    # get position from player
    print ( player + "s turn." )
    position = input ( "choose a position from 1 to 9:" )

    valid = False
    while not valid:

        while position not in ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9"]:
            position = input ( "Invalid input.Choose a position from 1 to 9:" )
        position = int ( position ) - 1

        if board[position] == "-":
            valid = True
        else:
            print ( "You cant go there.Go again." )

    board[position] = player

    display_board ( )


def check_if_game_over():
    check_for_winner ( )
    check_for_tie ( )


def check_for_winner():
    global winner
    # check raws
    row_winner = check_rows ( )
    # check columns
    column_winner = check_columns ( )
    # check diagonals
    diagonal_winner = check_diagonals ( )

    # get the winner
    if row_winner:
        # there was a win
        winner = row_winner
    elif column_winner:
        # there was a win
        winner = column_winner
    elif diagonal_winner:
        # there was a win
        winner = diagonal_winner
    else:
        # there was a no win
        winner = None
    return


def check_rows():
    global game_still_going
    # check if any of the raw have all same value(and is not empty
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row dose have a match,Flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return winner(O or X)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    # check if any of the raw have all same value(and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column dose have a match,Flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # return winner(O or X)
    if column_1:
        return board[0]
    elif column_2:
        return board[3]
    elif column_3:
        return board[6]
    else:
        return None


def check_diagonals():
    global game_still_going
    # check if any of the raw have all same value(and is not empty
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # if any row dose have a match,Flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    # return winner(O or X)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    else:
        return None


def check_for_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return


def flip_player():
    # global variable
    global current_player
    # if the current player was x,then change it to O
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


play_game ( )
