def lineHeuristic(board,piece,empty,winrowno):
    height = len(board)
    length = len(board[0])
    score = 0
    for y in range(height):
        for x in range(length):
            if board[y][x]==piece:
                
                #check hori
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x+i
                        y1 = y
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=piece or board[y1][x1]!=empty:
                            break
                        elif board[y1][x1]==piece:
                            inrow+=1
                    except:
                        break
                score+=inrow**1.25
                if inrow == winrowno-1:
                    score+=inrow
                #print("Coord: (%d,%d), Hori Score: %d"%(max(0,x+i),max(0,y),score))
                
                #check vert
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=piece or board[y1][x1]!=empty:
                            break
                        elif board[y1][x1]==piece:
                            inrow+=1
                    except:
                        break
                score+=inrow**1.25
                if inrow == winrowno-1:
                    score+=inrow
                #print("Coord: (%d,%d), Vert Score: %d"%(max(0,x),max(0,y+i),score))

                #check rightdiag
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x+i
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=piece or board[y1][x1]!=empty:
                            break
                        elif board[y1][x1]==piece:
                            inrow+=1
                    except:
                        break
                score+=inrow**1.25
                if inrow == winrowno-1:
                    score+=inrow
                #print("Coord: (%d,%d), Right Score: %d"%(max(0,x+i),max(0,y+i),score))
                
                #check leftdiag
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x-i
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=piece or board[y1][x1]!=empty:
                            break
                        elif board[y1][x1]==piece:
                            inrow+=1
                    except:
                        break
                score+=inrow**1.25
                if inrow == winrowno-1:
                    score+=inrow
                #print("Coord: (%d,%d), Left Score: %d"%(max(0,x-i),max(0,y-i),score))
    return score

def blockHeuristic(board,piece,empty,winrowno):
    height = len(board)
    length = len(board[0])
    score = 0
    for y in range(height):
        for x in range(length):
            if board[y][x]!=piece and board[y][x]!=empty:
                enemypiece = board[y][x]
                
                #check hori
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x+i
                        y1 = y
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x-i
                        y1 = y
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break

                #Check vert
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x
                        y1 = y-i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                    
                #check rightdiag
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x+i
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x-i
                        y1 = y-i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                    
                #check leftdiag
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x-i
                        y1 = y+i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break
                inrow = 0
                for i in range(winrowno):
                    try:
                        x1 = x+i
                        y1 = y-i
                        if x1<0 or y1<0:
                            assert(False)
                        if board[y1][x1]!=enemypiece:
                            if board[y1][x1] == piece:
                                score+=inrow**1.3
                                if inrow==winrowno-2:
                                    score+=inrow**1.6
                                break
                        else:
                            inrow+=1
                    except:
                        break

    return score**3

def openHeuristic(board,piece,empty,winrowno):
    height = len(board)
    length = len(board[0])
    score = 0
    for y in range(height):
        for x in range(length):
            cur_score = 0
            intruded = False
            if board[y][x]==piece:
                for i in range(winrowno):
                    cur_score = 0
                    y1 = max(0,y-i)
                    x1 = max(0,y-i)
                    y2 = min(height,y+i)
                    x2 = min(length,y+i)
                    for y3 in range(y1,y2):
                        for x3 in range(x1,x2):
                            if board[y3][x3] == empty:
                                cur_score+=1
                            else:
                                intruded = True
                    if intruded:
                        score += cur_score
                        break
    return score**0.35
                                
                            
import random
import copy
def evaluate(state,piece,heuristic = [lineHeuristic,blockHeuristic,openHeuristic]):
    board = state.getBoard()
    height = len(board)
    length = len(board[0])
    cur = 0
    for y in range(height):
        for x in range(length):
            if board[y][x] == state.emptypiece:
                temp = copy.deepcopy(board)
                temp[y][x] = piece
                score = 0
                for method in heuristic:
                    score += method(temp,piece,state.emptypiece,state.winNum)
                if score > cur:
                    cur = score
        return cur      
                    
def minmaxAgent (state,piece,heuristic = [lineHeuristic,blockHeuristic,openHeuristic],depth=1,easiness=1):

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

    def generateSuccessor(board,action,piece):
        temp = copy.deepcopy(board)
        height = len(board)
        length = len(board[0])
        temp[action[1]][action[0]] = piece
        return temp
    
    def explore(depth,max_depth,state,piece,a,b):
        if depth == 0: 
            return evaluate(state,piece,heuristic=heuristic)
        best = -666666 
        best_action = None
        board = state.getBoard()
        for action in getLegalActions(state,state.emptypiece):
            future = generateSuccessor(board,action,piece)
            new_state = copy.deepcopy(state)
            new_state.board = future
            score = enemy_explore(state.getPieces().index(piece)+1,depth-1,max_depth,new_state,piece,a,b)
            if score > best:
                best = score
                best_action = action
            a = max(a,best)
            if b < a*easiness:
                break
                    
        if depth != max_depth: 
            if best_action == None: 
                return evaluate(state,piece,heuristic=heuristic)
            return best
        else:
            return best_action
                        
        
    def enemy_explore(cur,depth,max_depth,state,piece,a,b):

            
        if cur%len(state.getPieces()) == state.getPieces().index(piece):
            return explore(depth,max_depth,state,piece,a,b)

        worst = 666666 
        worst_action = None
        board = state.getBoard()
        for action in getLegalActions(state,state.emptypiece):
            future = generateSuccessor(board,action,state.getPieces()[cur%len(state.getPieces())])
            new_state = copy.deepcopy(state)
            new_state.board = future    
            score = -1*(enemy_explore(cur+1,depth,max_depth,new_state,piece,a,b))
            if score < worst: 
                worst = score
                worst_action = action
  
            b = min(b,worst)
            if a*easiness > b:
                break
            
        if worst_action == None: 
            return evaluate(state,piece,heuristic=heuristic)
        return worst

    best = explore(depth,depth,state,piece,-666666,666666)
    if best == None:
        board = state.getBoard()
        height = len(board)
        length = len(board[0])
        best = (random.randint(0,length-1),random.randint(0,height-1))
        cur = 0
        for y in range(height):
            for x in range(length):
                if board[y][x] == state.emptypiece:
                    temp = copy.deepcopy(board)
                    temp[y][x] = piece
                    score = 0
                    for method in heuristic:
                        score += method(temp,piece,state.emptypiece,state.winNum)
                    if score != 0:
                        if score > cur:
                            best = (x,y)
                            cur = score
                        elif score == cur:
                            if random.randint(0,1)==1:
                                best = (x,y)
                                cur = score
        return best
    return best

