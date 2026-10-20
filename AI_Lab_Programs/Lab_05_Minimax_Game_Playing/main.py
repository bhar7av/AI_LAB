"""Lab 5: Minimax for Tic-Tac-Toe."""


def winner(board):
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]
    for a, b, c in lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    if " " not in board:
        return "draw"
    return None


def minimax(board, maximizing):
    """Evaluate a position; X maximizes the score and O minimizes it."""
    result = winner(board)
    if result == "X":
        return 1, None
    if result == "O":
        return -1, None
    if result == "draw":
        return 0, None

    best_move = None
    if maximizing:
        best_score = -float("inf")
        for move in range(9):
            if board[move] == " ":
                board[move] = "X"
                score, _ = minimax(board, False)
                board[move] = " "
                if score > best_score:
                    best_score, best_move = score, move
        return best_score, best_move

    best_score = float("inf")
    for move in range(9):
        if board[move] == " ":
            board[move] = "O"
            score, _ = minimax(board, True)
            board[move] = " "
            if score < best_score:
                best_score, best_move = score, move
    return best_score, best_move


def show_board(board):
    for row in range(0, 9, 3):
        print(" | ".join(board[row:row + 3]))
        if row < 6:
            print("--+---+--")


def main():
    board = [
        "X", "O", "X",
        "O", "X", " ",
        " ", " ", "O",
    ]
    print("Current board:")
    show_board(board)
    score, move = minimax(board, True)
    print("\nBest move for X:", move)
    print("Score:", score)
    if move is not None:
        board[move] = "X"
        print("\nBoard after X's move:")
        show_board(board)


if __name__ == "__main__":
    main()
