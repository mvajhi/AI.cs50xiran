"""
Tic Tac Toe Player
"""

from cmath import inf
import copy
import math
from queue import Empty

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
    num_X = int(0)
    num_O = int(0)

    # count X & O
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                num_X += 1
            elif board[i][j] == O:
                num_O += 1

    if num_X <= num_O:
        return X
    else:
        return O

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))

    return possible_actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action in actions(board):
        raise Exception("impassible action")

    new_board = copy.deepcopy(board)

    new_board[action[0]][action[1]] = player(board)

    return new_board

    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        counter_X = int(0)
        counter_O = int(0)
        for j in range(3):
            if board[i][j] == X:
                counter_X += 1
            elif board[i][j] == O:
                counter_O += 1
        if counter_X == 3:
            return X
        elif counter_O == 3:
            return O

    for j in range(3):
        counter_X = int(0)
        counter_O = int(0)
        for i in range(3):
            if board[i][j] == X:
                counter_X += 1
            elif board[i][j] == O:
                counter_O += 1
        if counter_X == 3:
            return X
        elif counter_O == 3:
            return O

    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[1][1]

    return None

    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == None:
                return False

    return True

    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    else:
        return 0

    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        return max_value(board)[1]
    else:
        return min_value(board)[1]

    raise NotImplementedError


def max_value(board):

    if terminal(board):
        return (utility(board), (0, 0))

    v = float(-inf)
    best_action = (0, 0)

    for action in actions(board):

        buffer_result = min_value(result(board, action))[0]

        if v < buffer_result:
            v = buffer_result
            best_action = action

        # best choice
        if v == 1:
            return (v, best_action)

    return (v, best_action)


def min_value(board):

    if terminal(board):
        return (utility(board), (0, 0))

    v = float(inf)
    best_action = (0, 0)

    for action in actions(board):

        buffer_result = max_value(result(board, action))[0]

        if v > buffer_result:
            v = buffer_result
            best_action = action

        # best choice
        if v == -1:
            return (v, best_action)

    return (v, best_action)
