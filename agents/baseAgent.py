from heuristics import *
from itertools import cycle,islice,dropwhile
from random import choice
class baseAgent(object):

    def __init__(self,state,piece,ordlist,heuristics=None,negligable=0.001):
        self.state = state
        self.piece = piece
        self.curPiece = ordlist[0]
        self.ordlist = ordlist
        self.heuristics = {lineHeuristic:{},blockHeuristic:{},openHeuristic:{}} if heuristics == None else heuristics
        self.negligable = negligable
        self.intMin = -2147483648
        self.intMax = 2147483647
        return

    #helper functions
    def getNextList(self,piece):
        return list(islice(dropwhile(lambda x:x!=piece,cycle(self.ordlist)),len(self.ordlist)))[1:]

    def fequal(self,float1,float2):
        return abs(float1 - float2) < self.negligable
    
    def reflexEvaluate(self,coord,piece=None,state=None,heuristics=None):
        if piece == None: piece = self.piece
        if state == None: state = self.state
        if heuristics == None: heuristics = self.heuristics
        score = 0
        for heuristic,config in heuristics.items(): score += heuristic(state,piece,coord,**config)
        return score

    #Extendables
    #setter
    def update(self,state,curPiece):
        self.state = state
        self.curPiece = curPiece
        return

    #Returns the move the agent makes
    #getter
    def getMove(self,state=None):
        if state != None: self.update(state,self.piece)
        else: state = self.state
        return choice(state.spaces())

    #for inheritors to implement
    def onWin(self,winner):
        pass
