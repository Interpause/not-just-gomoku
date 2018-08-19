import random
import copy
def evaluate_state(state,piece,heuristic = [lineHeuristic,blockHeuristic,openHeuristic]):
    height = state.height
    length = state.length
    cur = 0
    for y in range(height):
        for x in range(length):
            if board[y][x] == state.emptypiece:
                score = evaluate_action(state,piece,x,y,heuristic)
                if score > cur:
                    cur = score
        return cur

def evaluate_action(state,piece,x,y,heuristic = [lineHeuristic,blockHeuristic,openHeuristic]):
    temp = state.getBoard()
    temp[y][x] = piece
    score = 0
    for method in heuristic:
        score += method(temp,piece,state.emptypiece,state.winNum)
    return score

def newAgent(state,piece,heuristic = []):

    def getLegalActions(state,empty):
        if state.isWin() != state.emptypiece:
            return []
        board = state.getBoard()
        height = len(board)
        length = len(board[0])
        possible = []
        for y in range(height):
            for x in range(length):
                if board[y][x]==empty:
                    possible.append((x,y))
        return possible

    #main code
    
    
def openHeuristic(board,piece,empty,winrowno):
    height = len(board)
    length = len(board[0])
    score = 0
    for y in range(height):
        for x in range(length):
            cur = 0
            blocked = False
            if board[y][x]==piece:
                for i in range(winrowno):
                    cur_score = 0
                    y1 = max(0,y-i)
                    x1 = max(0,y-i)
                    y2 = min(height,y+i)
                    x2 = min(length,y+i)
                    for y3 in range(y1,y2):
                        for x3 in range(x1,x2):
                            if board[y3][x3] == empty or board[y3][x3] == piece:
                                cur_score+=1
                            else:
                                intruded = True
                    if intruded:
                        score += cur_score
                        break
    return score**0.35
