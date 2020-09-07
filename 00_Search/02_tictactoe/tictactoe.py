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
    countX = 0
    countO = 0

    for row in board:
        for cell in row:
            if cell == X:
                countX +=1
            elif cell == O:
                countO += 1

    #print("Os:",countO)
    #print("Xs:",countX)

    if countX > countO :
        #print("next game to O")
        return "O"
    else:
        #print("next game to X")
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possibleActions.add((i, j))

    # print (possibleActions)
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    resultingBoard = copy.deepcopy(board)
    i,j = action
    # print(i,j)

    if board[i][j] == EMPTY:
        resultingBoard[i][j] = player(board)
    else:
        print("Error exception should be raised here")

    # print(board)
    # print(resultingBoard)   
    return resultingBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    winnerValue = None
    # X case
    # rows
    for row in board:
        if winnerValue is not None:
            return winnerValue
        winnerValue = X
        for cell in row:
            if cell == O or cell == EMPTY:
                winnerValue = None

    # columns
    for j in range(len(board)):
        if winnerValue is not None:
            return winnerValue
        winnerValue = X
        for i, row in enumerate(board):
            if row[j] == O or row[j] == EMPTY:
                winnerValue = None
    
    # diagonals
    if (board[0][0] == X and board[1][1] == X and board[2][2] == X) or (board[2][0] == X and board[1][1] == X and board[0][2] == X):
        winnerValue = X
        return winnerValue
    
    # O case
    # rows
    for row in board:
        if winnerValue is not None:
            return winnerValue
        winnerValue = O
        for cell in row:
            if cell == X or cell == EMPTY:
                winnerValue = None

    # columns
    for j in range(len(board)):
        if winnerValue is not None:
            return winnerValue
        winnerValue = O
        for i, row in enumerate(board):
            if row[j] == X or row[j] == EMPTY:
                winnerValue = None
    
    # diagonals
    if (board[0][0] == O and board[1][1] == O and board[2][2] == O) or (board[2][0] == O and board[1][1] == O and board[0][2] == O):
        winnerValue = O
        return winnerValue
    
    return winnerValue 
  
  
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False

    return True

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
    if terminal(board):
        return None

    nextAction = None
    
    # maximizing player:
    if player(board) == X:
        maxValue = -2 
        for action in actions(board):
            value = min_value(result(board,action))
            if value > maxValue:
                maxValue = value
                nextAction = action
                if maxValue == 1:
                    return nextAction

        if nextAction is not None:
            return nextAction

    # minimizing player:
    elif player(board) == O:
        minValue = 2        
        for action in actions(board):
            value = max_value(result(board,action))
            if value < minValue:
                minValue = value
                nextAction = action
                if minValue == -1:
                    return nextAction
        if nextAction is not None:
            return nextAction
    return None
    
def max_value(state):
    v = -2
    if terminal(state):
        return utility(state)
    for action in actions(state):
        if v == 1:
            return v
        v = max(v, min_value(result(state,action)))
    return v

def min_value(state):
    v = 2
    if terminal(state):
        return utility(state)
    for action in actions(state):
        if v == -1:
            return v
        v = min(v, max_value(result(state,action)))
    return v    

def main():
    
    board = initial_state()
    print(board)
    player(board)
    actions(board)
    newboard = result(board,(0,0))
    result(newboard,(0,1))
    print(board)
    print(winner(board))
    print("ended:",terminal(board))
    print("utility",utility(board))
    

if __name__ == "__main__":
    main()
