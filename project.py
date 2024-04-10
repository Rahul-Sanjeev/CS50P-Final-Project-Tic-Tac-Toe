# Main function
def main():
    board = "\n|1|2|3|\n|4|5|6|\n|7|8|9|\n"
    display_board(board)
    while True:
        board = playerX_turn(board)
        if game_won(board):
            print("Player X wins!")
            break
        elif is_draw(board):
            print("Draw!")
            break
        board = playerO_turn(board)
        if game_won(board):
            print("Player O wins!")
            break
        elif is_draw(board):
            print("Draw!")
            break

# Display board
def display_board(board):
    print(board)


# Player X turn
def playerX_turn(board):
    pos = input("Player X, Your Turn: ")
    if is_valid(pos, board):
        board = board.replace(pos, "X")
        display_board(board)
        return board
    else:
        print("Position Not Valid")
        return playerX_turn(board)


# Player O turn
def playerO_turn(board):
    pos = input("Player O, Your Turn: ")
    if is_valid(pos, board):
        board = board.replace(pos, "O")
        display_board(board)
        return board
    else:
        print("Position Not Valid")
        return playerO_turn(board)


# Check if pos is valid
def is_valid(pos, board):
    board_pos = [2, 4, 6, 10, 12, 14, 18, 20, 22]
    for i in board_pos:
        if pos == board[i]:
            return True
    return False


# Game winning condition
def game_won(board):
    if (
        board[2] == board[4] == board[6]
        or board[10] == board[12] == board[14]
        or board[18] == board[20] == board[22]
        or board[2] == board[10] == board[18]
        or board[4] == board[12] == board[20]
        or board[6] == board[14] == board[22]
        or board[2] == board[12] == board[22]
        or board[6] == board[12] == board[18]
    ):
        return True
    return False


# If draw
def is_draw(board):
    board_pos = [2, 4, 6, 10, 12, 14, 18, 20, 22]
    for i in board_pos:
        if board[i] != "X" and board[i] != "O":
            return False
    return True



if __name__ == "__main__":
    main()
