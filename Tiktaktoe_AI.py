import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board): 
    return [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, "O"):
        return 1  # AI wins
    if check_win(board, "X"):
        return -1  # Human wins
    if check_draw(board):
        return 0  # Draw

    if is_maximizing:
        best_score = -math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = "O"
            score = minimax(board, depth + 1, False)
            board[r][c] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (r, c) in get_available_moves(board):
            board[r][c] = "X"
            score = minimax(board, depth + 1, True)
            board[r][c] = " "
            best_score = min(score, best_score)
        return best_score

def ai_move(board):
    best_score = -math.inf
    best_move = None
    for (r, c) in get_available_moves(board):
        board[r][c] = "O"
        score = minimax(board, 0, False)
        board[r][c] = " "
        if score > best_score:
            best_score = score
            best_move = (r, c)
    return best_move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human = "X"
    ai = "O"
    current_turn = human

    while True:
        print_board(board)
        if current_turn == human:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if board[row][col] == " ":
                board[row][col] = human
                if check_win(board, human):
                    print_board(board)
                    print("You win!")
                    break
                elif check_draw(board):
                    print_board(board)
                    print("It's a draw!")
                    break
                current_turn = ai
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is making its move...")
            row, col = ai_move(board)
            board[row][col] = ai
            if check_win(board,ai):
                print_board(board)
                print("AI wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            current_turn = human

if __name__ == "__main__":
    play_game()