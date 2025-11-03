def play(board):
    """
    Rule-based AI that decides the best move for 'o' (the AI).
    Input:
        board = list of 9 strings ['x', 'o', '', '', 'x', '', 'o', '', '']
    Output:
        integer (0–8) position where AI wants to play, or None if full.
    """
    ai = 'o'         # AI symbol
    opponent = 'x'   # Human player symbol

    # All possible 3-in-a-row winning combinations on the 3x3 board
    wins = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Middle column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal top left to right
        [2, 4, 6]   # Diagonal top right to left
    ]

    # 1. AI tries to win
    for a, b, c in wins:
        # a, b, c are positions in one possible winning line
        # Example: a=0, b=1, c=2 means top row
        # Another Example: a=1, b=4, c=7 means middle column

        line = [board[a], board[b], board[c]]  # Get symbols in that line
        if line.count(ai) == 2 and line.count('') == 1:
            # If AI has 2 in that line and one empty spot, take the empty spot
            return [a, b, c][line.index('')]

    # 2. AI tries to block opponent from winning ---
    for a, b, c in wins:
        line = [board[a], board[b], board[c]]
        if line.count(opponent) == 2 and line.count('') == 1:
            return [a, b, c][line.index('')]

     # 3. Take center if available
    if board[4] == '':
        return 4

    # 4.Take a corner if available
    for i in [0, 2, 6, 8]:
        if board[i] == '':
            return i

    # 5.Take any remaining side
    for i in [1, 3, 5, 7]:
        if board[i] == '':
            return i

    # 6. No moves left (draw)
    return None


