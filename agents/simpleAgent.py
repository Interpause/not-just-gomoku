from heuristics import *
def simpleAgent(state,piece,ordlist,heuristics = [lineHeuristic,blockHeuristic]):
    best = (0,0)
    cur = -9999999
    for space in state.spaces():
        score = 0
        for heuristic in heuristics:
            score += heuristic(state,piece,space)
        if score > cur:
            cur = score
            best = space
    print("%s SCORE RN %d"%(piece,cur))
    return best
                    
