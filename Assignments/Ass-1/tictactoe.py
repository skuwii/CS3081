"""
Tic Tac Toe Player
"""

import math
import copy

#These are the possible varuables.

X = "X"
O = "O"
EMPTY = None



def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    Xcount = 0
    Ocount = 0
    
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                Xcount += 1
            elif board[i][j] == "O":
                Ocount += 1

    if Xcount == Ocount:
        return X
    else:
        return O
    
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible = set() # Here I used set insted of list in order to avoid duplicates.
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY :
                possible.add((i,j))
    return possible
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    i, j = action
    new_board[i][j] = player(board)

    return new_board
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3): # Here for checking the row's
        if board[i][0] is not EMPTY and board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]

    for j in range(3): # Here for checking the column's
        if board[0][j] is not EMPTY and board[0][j] == board[1][j] == board[2][j]:
            return board[0][j]
        
    if board[0][0] is not EMPTY and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] is not EMPTY and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]

    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Here it should not depends on the utility, it should use the winner(board) function
    if winner(board) is not None: # It means that there is a winner
        return True 

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY: # Here if there any cell is still empty, the game not over yet
                return False  
    return True  # This is if no winner and no empty cell (draw)

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else: 
        return 0

    raise NotImplementedError



def minimax(board):
    """Returns the optimal action for the current player."""
    if terminal(board):
        return None

    if player(board) == X:  # X is maximizing
        best_val = -float('inf')
        best_action = None
        for action in actions(board):
            val = min_value(result(board, action))
            if val > best_val:
                best_val = val
                best_action = action
        return best_action
    else:  # O is minimizing
        best_val = float('inf')
        best_action = None
        for action in actions(board):
            val = max_value(result(board, action))
            if val < best_val:
                best_val = val
                best_action = action
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -float('inf')
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
