largenum = (10**4)*2
winbonus = 1*largenum
dangerbonus = 1.01*largenum
fatalbonus = 1.21*largenum
#best one i could conceive
def lineHeuristic(state,piece,coord):
    #mul should be -1, 0 or 1 only. Else interesting behaviour (new mechanic?)
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            maxlen = 1
            actlen = 1
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if x >= state.length() or y >= state.height() or x < 0 or y < 0:
                    break
                spot = grid[y][x]
                if spot == piece:
                    actlen += 1
                elif spot == None:
                    pass
                else:
                    break
                maxlen += 1
            return (maxlen,actlen)
        
        def evaluate(maxlen,actlen):
            score = 0
            if actlen == state.winnum():
                score += winbonus
            if maxlen >= state.winnum() and state.winnum() > actlen and actlen > 1:
                score += int((actlen/state.winnum()*10)**4)
            return score
        
        dir1 = count(grid,xmul,ymul)
        dir2 = count(grid,-xmul,-ymul)
        return evaluate(dir1[0]+dir2[0]-1,dir1[1]+dir2[1]-1)
        
    tscore = 0
    grid = state.grid()

    tscore += score(grid,1,0)
    if tscore >= winbonus:
        return tscore
    tscore += score(grid,0,1)
    if tscore >= winbonus:
        return tscore
    tscore += score(grid,1,1)
    if tscore >= winbonus:
        return tscore
    tscore += score(grid,1,-1)

    return tscore

def blockHeuristic(state,piece,coord):
    score = 0
    grid = state.grid()
    #mul should be -1, 0 or 1 only. Else interesting behaviour (new mechanic?)
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            maxlen = 0
            actlen = 0
            blocked = False
            cur_op = None
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if x >= state.length() or y >= state.height() or x < 0 or y < 0:
                    break
                spot = grid[y][x]
                if spot == piece:
                    break
                elif spot != None:
                    if cur_op == None:
                        cur_op = spot
                    elif spot != cur_op:
                        break
                    actlen += 1
                maxlen += 1
            return (maxlen,actlen)
        
        def evaluate(maxlen,actlen):
            score = 0
            if maxlen >= state.winnum():
                score += int((((actlen/state.winnum()))*10)**4)
            return score
        
        dir1 = count(grid,xmul,ymul)
        dir2 = count(grid,-xmul,-ymul)
        return evaluate(dir1[0]+dir2[0],dir1[1]+dir2[1])
        
    tscore = 0
    grid = state.grid()

    tscore += score(grid,1,0)
    tscore += score(grid,0,1)
    tscore += score(grid,1,1)
    tscore += score(grid,1,-1)

    return tscore*2

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
