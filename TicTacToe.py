board = [[' ' for i in range(3)] for j in range(3)]

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for i in range(3):
        print("|       " * 3, "|", sep="")
        for j in range(3):
            value = board[i][j]
            if value == " ":
                value = i * 3 + j + 1
            print(f"|   {value}   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def start():
    while True:
        answer = input("Would you like to start? ")
        if answer.lower() == "yes":
            player_symbol = "X"
            ai_symbol = "O"
            current_turn = "player"
            break
        elif answer.lower() == "no":
            player_symbol = "O"
            ai_symbol = "X"
            current_turn = "ai"
            break
        else:
            print("Answer with \"yes\" or \"no\".")
            continue
    return player_symbol, ai_symbol, current_turn

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != " ":
            return board[0][j]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    return None

def is_board_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True

def player_move(board, player_symbol):
    while True:
        move = input("Choose a position (1-9): ")
        if not move.isdigit():
            print("Only digits allowed!")
            continue
        move = int(move)
        if move < 1 or move > 9:
            print("Invalid position!")
            continue
        i = (move - 1) // 3
        j = (move - 1) % 3
        if board[i][j] != " ":
            print("Position taken!")
            continue
        board[i][j] = player_symbol
        break

def minimax(board, is_maximizing, player_symbol, ai_symbol):
    rez = check_winner(board)
    if rez == player_symbol:
        return -1
    elif rez == ai_symbol:
        return 1
    if is_board_full(board):
        return 0
    if is_maximizing == True:
        best_score = -100
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol
                    score = minimax(board, False, player_symbol, ai_symbol)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = 100
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player_symbol
                    score = minimax(board, True, player_symbol, ai_symbol)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_ai_move(board, player_symbol, ai_symbol):
    best_score = -100
    best_move = None
    if all(board[i][j] == " " for i in range(3) for j in range(3)):
        return (1, 1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_symbol
                score = minimax(board, False, player_symbol, ai_symbol)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

player_symbol, ai_symbol, current_turn = start()
while True:
    if current_turn == "player":
        display_board(board)
        player_move(board, player_symbol)
    else:
        i, j = best_ai_move(board, player_symbol, ai_symbol)
        board[i][j] = ai_symbol
    rez = check_winner(board)
    if rez == ai_symbol:
        display_board(board)
        print("AI won!")
        break
    elif rez == player_symbol:
        display_board(board)
        print("You won!")
        break
    elif is_board_full(board):
        display_board(board)
        print("It's a tie!")
        break
    if current_turn == "player":
        current_turn = "ai"
    else:
        current_turn = "player"