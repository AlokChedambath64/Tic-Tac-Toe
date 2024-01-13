"""
Tic Tac Toe Player
"""

import math
import copy

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
    count_X = 0
    count_O = 0
    # check how many X and O are present in the board
    for list in board:
        for i in list:
            if i == X:
                count_X += 1
            if i == O:
                count_O += 1
    # check if there are more Xs than Os
    if count_X > count_O:
        return O
    
    return X
       

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()

    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == EMPTY:
                moves.add((i,j))
            
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # check if action is valid
    actions1 = actions(board)

    #print("Valid Actions:", actions1)
    #print("Provided Action:", action)

    if action not in actions1:
        raise ValueError
    
    # make changes to the board
    newboard = copy.deepcopy(board)

    newboard[action[0]][action[1]] = player(board)
    
    return newboard


def winner(board):

    # Check rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] is not None:
            return row[0]

    # Check columns
    for col_index in range(len(board[0])):
        column_values = [row[col_index] for row in board]
        if all(cell == column_values[0] for cell in column_values) and column_values[0] is not None:
            return column_values[0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    moves = actions(board)

    if len(moves) == 0:
        return True
    
    if winner(board) != None:
        return True
    
    return False


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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #check if board is terminal
    if terminal(board):
        return None
    else:
        #to check whether to max or min
        if player(board) == X:
            val, move = max_value(board)
            return move
        else:
            val, move = min_value(board)
            return move


def max_value(board):
    # base case
    if terminal(board):
        return utility(board), None

    # initalizing the v and move value for each time the function gets called so as to best move in that scenario
    v = float('-inf')
    move = None
    # To compare for each possible move
    for action in actions(board):

        val, action1 = min_value(result(board, action))

        if val > v:
            v = val
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):

        val, action1 = max_value(result(board, action))
        if val < v:
            v = val
            move = action
            if v == -1:
                return v, move

    return v, move
    