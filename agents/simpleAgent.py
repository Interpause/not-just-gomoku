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
                score+=inrow**1.4
                if inrow == winrowno-1:
                    score+=inrow**5
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
                score+=inrow**1.4
                if inrow == winrowno-1:
                    score+=inrow**5
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
                score+=inrow**1.4
                if inrow == winrowno-1:
                    score+=inrow**5
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
                score+=inrow**1.4
                if inrow == winrowno-1:
                    score+=inrow**5
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
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
                                score+=inrow**1.1
                                if inrow==winrowno-2:
                                    score+=inrow**2
                                break
                        else:
                            inrow+=1
                    except:
                        break

    return score

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
    return score**0.25
                                
                            
import random
import copy
def simpleAgent(state,piece,heuristic = [lineHeuristic,blockHeuristic,openHeuristic]):
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
                    
