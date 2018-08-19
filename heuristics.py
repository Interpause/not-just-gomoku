#defaults
multiplier = 10
exponent = 4
largenum = 10**4
winbonus = largenum*2 #twice max of actlen/state.winnum

#helpers
def isOut(state,x,y):
    if x >= state.length() or y >= state.height() or x < 0 or y < 0: return True
    return False

#heuristics
def lineHeuristic(state,piece,coord,weight=1,multiplier=multiplier,exponent=exponent,winbonus=winbonus):
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            maxlen = 1
            actlen = 1
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if isOut(state,x,y): break
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
            if maxlen >= state.winnum() and state.winnum() > actlen > 1:
                score += (actlen/state.winnum()*multiplier)**exponent
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

    return tscore*weight

def blockHeuristic(state,piece,coord,weight=2,multiplier=multiplier,exponent=exponent):
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            maxlen = 0
            actlen = 0
            cur_op = None
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if isOut(state,x,y): break
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
                score += (actlen/state.winnum()*multiplier)**exponent
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

    return tscore*weight

#incomplete
def clusterHeuristic(state,piece,coord,weight=0.5,multiplier=multiplier,exponent=exponent):
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            maxlen = 0
            actlen = 0
            cur_op = None
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if isOut(state,x,y): break
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
                score += int((((actlen/state.winnum()))*multiplier)**exponent)
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

    return tscore*weight

def openHeuristic(state,piece,coord,weight=10,multiplier=1,exponent=3):
    def score(grid,xmul,ymul):
        def count(grid,xmul,ymul):
            space = 0
            for i in range(1,state.winnum()):
                x = coord[0]+i*xmul
                y = coord[1]+i*ymul
                if isOut(state,x,y): break
                spot = grid[y][x]
                if spot == None: space+=1
                else: break
            return space
        
        def evaluate(space):
            score = 0
            score += (space/state.winnum()*multiplier)**exponent
            return score
        
        dir1 = count(grid,xmul,ymul)
        dir2 = count(grid,-xmul,-ymul)
        return evaluate(dir1+dir2)
     
    tscore = 0
    grid = state.grid()

    tscore += score(grid,1,0)
    tscore += score(grid,0,1)
    tscore += score(grid,1,1)
    tscore += score(grid,1,-1)

    return tscore*weight
