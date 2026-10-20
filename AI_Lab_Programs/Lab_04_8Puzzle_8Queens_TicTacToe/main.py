"""Lab 4: 8-puzzle BFS, 8-queens backtracking, and Tic-Tac-Toe minimax."""

from collections import deque


def solve_8_puzzle(start, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
    """Find a shortest move sequence for a solvable 8-puzzle using BFS."""
    start = tuple(start)
    goal = tuple(goal)
    queue = deque([start])
    parent = {start: None}

    while queue:
        state = queue.popleft()
        if state == goal:
            path = []
            while state is not None:
                path.append(state)
                state = parent[state]
            return list(reversed(path))

        blank = state.index(0)
        row, col = divmod(blank, 3)
        possible = []
        if row > 0:
            possible.append(blank - 3)
        if row < 2:
            possible.append(blank + 3)
        if col > 0:
            possible.append(blank - 1)
        if col < 2:
            possible.append(blank + 1)

        for swap_index in possible:
            next_state = list(state)
            next_state[blank], next_state[swap_index] = (
                next_state[swap_index], next_state[blank]
            )
            next_state = tuple(next_state)
            if next_state not in parent:
                parent[next_state] = state
                queue.append(next_state)
    return None


def solve_8_queens(size=8):
    """Return one solution as a list: row index for the queen in each column."""
    queens = []

    def place_queen(column):
        if column == size:
            return True
        for row in range(size):
            safe = True
            for previous_col, previous_row in enumerate(queens):
                if row == previous_row or abs(row - previous_row) == abs(column - previous_col):
                    safe = False
                    break
            if safe:
                queens.append(row)
                if place_queen(column + 1):
                    return True
                queens.pop()
        return False

    return queens if place_queen(0) else None


def print_board(queens):
    for row in range(len(queens)):
        print(" ".join("Q" if queens[col] == row else "." for col in range(len(queens))))


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


def minimax(board, is_maximizing):
    """Return (score, best_index) from X's point of view."""
    result = winner(board)
    if result == "X":
        return 1, None
    if result == "O":
        return -1, None
    if result == "draw":
        return 0, None

    best_index = None
    if is_maximizing:
        best_score = -float("inf")
        for index, cell in enumerate(board):
            if cell == " ":
                board[index] = "X"
                score, _ = minimax(board, False)
                board[index] = " "
                if score > best_score:
                    best_score, best_index = score, index
        return best_score, best_index
    else:
        best_score = float("inf")
        for index, cell in enumerate(board):
            if cell == " ":
                board[index] = "O"
                score, _ = minimax(board, True)
                board[index] = " "
                if score < best_score:
                    best_score, best_index = score, index
        return best_score, best_index


def main():
    print("8-Puzzle:")
    # This start state is two moves away from the goal.
    puzzle_path = solve_8_puzzle((1, 2, 3, 4, 5, 6, 0, 7, 8))
    if puzzle_path:
        print("Moves required:", len(puzzle_path) - 1)
        for state in puzzle_path:
            print(state[:3], state[3:6], state[6:])
    else:
        print("No solution found.")

    print("\n8-Queens:")
    queens = solve_8_queens()
    print("Queen row per column:", queens)
    print_board(queens)

    print("\nTic-Tac-Toe:")
    board = [
        "X", "O", "X",
        " ", "O", " ",
        " ", " ", " ",
    ]
    score, move = minimax(board, True)
    print("Board:", board)
    print("Best move for X (index 0-8):", move)
    print("Minimax score:", score)


if __name__ == "__main__":
    main()
