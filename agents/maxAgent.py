from itertools import cycle,islice,dropwhile
from copy import deepcopy
from heuristics import *
#Yay, its actually smarter than simpleAgent unlike the old version. Now... Well it needs to be optimized for speed. 
def maxAgent(state,piece,ordpieces,heuristics = [lineHeuristic,blockHeuristic], finLayer=1,dim=0.95,*args,**kwargs):

    #reflex evaluation
    def evaluate(state,piece):
        best = (0,0)
        cur = -9999999
        for space in state.spaces():
            score = reflex(state,piece,space)
            if score > cur:
                cur = score
                best = space
        return (best,cur)

    def reflex(state,piece,space):
        score = 0
        for heuristic in heuristics:
            score += heuristic(state,piece,space)
        return score
    
    #had to start annotating cause i am literally mentally coming up with this no tutorial
    def getOptimal(state,piece,curLayer=0):
        if curLayer == finLayer:
            return evaluate(state,piece)

        best = (0,0)
        cur = -9999999
        for space in state.spaces():
            
            score = 0
            score += reflex(state,piece,space)
            #filtering
            if score < cur*(1-dim):
                continue
            
            #shared among each turn of players (cause references are useful)
            dupe = deepcopy(state)
            dupe.place(piece,space) #its testing move
                        
            #turn list starting after its own play
            others = list(islice(dropwhile(lambda x:x!=piece,cycle(ordpieces)),len(ordpieces)))[1:]

            #simulates how enemy (in order of course) would place using same algorithm
            for other in others:
                enemy = getOptimal(dupe,other,curLayer+1)
                if enemy[1] < 0:
                    break
                dupe.place(other,enemy[0])

            
            #using dupe state, sees future move viability
            score += getOptimal(dupe,piece,curLayer+1)[1]*dim
            #print(future)
            if score > cur:
                cur = score
                best = space
            if cur < 0:
                best = space
                
        return (best,cur)
            
    return getOptimal(state,piece)[0]
    
