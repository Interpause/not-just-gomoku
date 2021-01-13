from heuristics import *
from itertools import cycle,islice,dropwhile
from random import choice

class baseAgent(object):
    '''base class that all game agents should extend and override.

    Attributes:
        state (state): The current game state seen by the agent, see state.py for more details.
        piece (str): The piece that the agent uses. Doubles as both what is printed and its id.
        curPiece (str): The current piece in play. Doubles as a way to check whose turn it is.
        ordlist (str[]): The order that pieces should play in.
        heuristics (dict): A dict where keys are the heuristic function, and values are a dict of kwargs for that function.
        negligable (float): Threshold between which two floats are considered equal.
        intMin (float): Unused.
        intMax (float): Unused.
    '''

    def __init__(self,state,piece,ordlist,heuristics=None,negligable=0.001):
        '''Constructor for baseAgent that should be extended.

        Args:
            state (state): The initial game state, see state.py for more details.
            piece (str): The piece that the agent uses. Doubles as both what is printed and its id.
            ordlist (str[]): The order that pieces should play in.
            heuristics (dict): Defaults to None for {lineHeuristic:{},blockHeuristic:{},openHeuristic:{}}.
            negligable (float): Defaults to 0.001.
        '''

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
        '''Get the subsequent order of pieces using self.ordlist and the piece provided.'''

        return list(islice(dropwhile(lambda x:x!=piece,cycle(self.ordlist)),len(self.ordlist)))[1:]

    def fequal(self,float1,float2):
        '''Compare if two floats are roughly equal using self.negligable.'''

        return abs(float1 - float2) < self.negligable
    
    def reflexEvaluate(self,coord,piece=None,state=None,heuristics=None):
        '''Shallow evaluates the reward for an action.'''
        if piece == None: piece = self.piece
        if state == None: state = self.state
        if heuristics == None: heuristics = self.heuristics
        score = 0
        for heuristic,config in heuristics.items(): score += heuristic(state,piece,coord,**config)
        return score

    #Extendables
    #setter
    def update(self,state,curPiece):
        '''Function to update the turn and game state for the agent. Can be overrided to perform preprocessing.'''

        self.state = state
        self.curPiece = curPiece
        return

    #Returns the move the agent makes
    #getter
    def getMove(self,state=None):
        '''Function that is called to get the decision made by the agent. Should be overrided. '''

        if state != None: self.update(state,self.piece)
        else: state = self.state
        return choice(state.spaces())

    #for inheritors to implement
    def onWin(self,winner):
        '''Function that is called when a piece wins, with winner being the piece. Used by markovAgent.py to save the heuristic configuration.'''

        pass
