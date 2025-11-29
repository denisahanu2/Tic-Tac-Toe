import math

def display_board(board):
    print("+-------" * 3, "+", sep="")
    for i in range(3):
        print("|       " * 3, "|", sep="")
        for j in range(3):
            if board[i][j] == " ":
                value = i * 3 + j + 1
                print(f"|   {value}   ", end="")
            else:
                print(f"|   {board[i][j]}   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def start():
    # initializes the game and determines who starts
    while True:
        answer = input("Would you like to start? ").lower()
        if answer == "yes":
            return "X", "O", "player"
        elif answer == "no":
            return "O", "X", "ai"
        else:
            print("Please answer with \"yes\" or \"no\"!")

def check_winner(board):
    # verifies if there's a winner

    # verifies for rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    #verifies for diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None

def is_full(board):
    #verifies if the table is full
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def player_move(board, player_symbol):
    # makes the player's move
    while True:
        value = input("Choose a position (1-9): ")
        if not value.isdigit():
            print("Only digits allowed!")
            continue

        value = int(value)
        if value < 1 or value > 9:
            print("The position given is not valid!")
            continue

        row = (value - 1) // 3
        col = (value - 1) % 3

        if board[row][col] != " ":
            print("The position is taken!")
            continue

        board[row][col] = player_symbol
        break

def minimax(board, is_maximizing, player_symbol, ai_symbol):
    # minimax algorithm
    rez = check_winner(board)
    if rez == player_symbol:
        return -1
    elif rez == ai_symbol:
        return 1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol
                    score = minimax(board, False, player_symbol, ai_symbol)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player_symbol
                    score = minimax(board, True, player_symbol, ai_symbol)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_ai_move(board, player_symbol, ai_symbol):
    # determines AI's best move
    # optimization: if the table is empty, it takes the middle
    if all(board[i][j] == " " for i in range(3) for j in range(3)):
        return (1, 1)

    best_score = -math.inf
    best_move = None

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

def main():
    board = [[" " for i in range(3)] for j in range(3)]
    player_symbol, ai_symbol, current_turn = start()

    while True:
        if current_turn == "player":
            display_board(board)
            player_move(board, player_symbol)
        else:
            print(f"AI ({ai_symbol}) is thinking...")
            move = best_ai_move(player_symbol, ai_symbol)
            if move:
                i, j = move
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
        elif is_full(board):
            display_board(board)
            print("It's a tie!")
            break

        # change of turns
        if current_turn == "player":
            current_turn = "ai"
        else:
            current_turn = "player"

if __name__ == "__main__":
    main()