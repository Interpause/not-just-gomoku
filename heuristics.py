largenum = 1000000
winbonus = 1*largenum
dangerbonus = 1.01*largenum
fatalbonus = 1.21*largenum
#best one i could conceive
def lineHeuristic(state,piece,coord):
    score = 0
    grid = state.grid()
    #check hori
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]
        if x >= state.length():
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]
        if x < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    if actlen == state.winnum():
        return winbonus
    if potlen >= state.winnum() and actlen > 1:
        score += int((actlen/state.winnum()*100)**2)
    #print("HORI POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
    #check vert
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]
        y = coord[1]+i
        if y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]
        y = coord[1]-i
        if y < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    if actlen == state.winnum():
        return winbonus
    if potlen >= state.winnum() and actlen > 1:
        score += int((actlen/state.winnum()*100)**2)
    #print("VERT POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
    #check rdiag
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]+i
        if x >= state.length() or y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]-i
        if x < 0 or y < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    if actlen == state.winnum():
        return winbonus
    if potlen >= state.winnum() and actlen > 1:
        score += int((actlen/state.winnum()*100)**2)
    #print("RDIAG POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))    
    #check ldiag
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]-i
        if y < 0 or x >= state.length():
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
            break
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]+i
        if x < 0 or y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            actlen += 1
        elif spot == None:
            pass
        else:
             break
        potlen += 1        
    if actlen == state.winnum():
        return winbonus
    if potlen >= state.winnum() and actlen > 1:
        score += int((actlen/state.winnum()*100)**2)
    #print("LDIAG POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
    return score

#-2 when low priority end game, -1 when game over. logic fails on 3x3 (unsupported)
def blockHeuristic(state,piece,coord):
    score = 0
    grid = state.grid()
    #check hori
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]
        if x >= state.length():
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]
        if x < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    if actlen == state.winnum()-1:
        return fatalbonus
    if actlen == state.winnum()-2:
        return dangerbonus
    if actlen == state.winnum():
        return 0
    if potlen >= state.winnum():
        score += int((actlen/state.winnum()*99)**2)
    #print("HORI POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
    #check vert
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]
        y = coord[1]+i
        if y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]
        y = coord[1]-i
        if y < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    if actlen == state.winnum()-1:
        return fatalbonus
    if actlen == state.winnum()-2:
        return dangerbonus
    if actlen == state.winnum():
        return 0
    if potlen >= state.winnum():
        score += int((actlen/state.winnum()*99)**2)
    #print("VERT POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
    #check rdiag
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]+i
        if x >= state.length() or y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]-i
        if x < 0 or y < 0:
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    if actlen == state.winnum()-1:
        return fatalbonus
    if actlen == state.winnum()-2:
        return dangerbonus
    if actlen == state.winnum():
        return 0
    if potlen >= state.winnum():
        score += int((actlen/state.winnum()*99)**2)
    #print("RDIAG POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))    
    #check ldiag
    potlen = 1
    actlen = 1
    for i in range(1,state.winnum()):
        x = coord[0]+i
        y = coord[1]-i
        if y < 0 or x >= state.length():
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1
    for i in range(1,state.winnum()):
        x = coord[0]-i
        y = coord[1]+i
        if x < 0 or y >= state.height():
            break
        spot = grid[y][x]
        if spot == piece:
            break
        elif spot != None:
            actlen += 1
        potlen += 1        
    if actlen == state.winnum()-1:
        return fatalbonus
    if actlen == state.winnum()-2:
        return dangerbonus
    if actlen == state.winnum():
        return 0
    if potlen >= state.winnum():
        score += int((actlen/state.winnum()*99)**2)
    #print("LDIAG POTLEN %d, ACTLEN %d, CURRENT SCORE %d" %(potlen,actlen,score))
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
    return score**0.35
