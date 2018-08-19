from agents.baseAgent import baseAgent
from pickle import dumps,loads
from heuristics import *
class markovAgent(baseAgent):

    def __init__(self,*args,filepath="agents/markovSimpleAgent.pkl",heuristics=None,**kwargs):
        self.filepath = filepath
        
        try:
            with open(self.filepath,'rb') as f: heuristics = loads(f.read())
        except Exception: pass
        if heuristics == None: heuristics = {lineHeuristic:{'multiplier':10,'exponent':4,'weight':1,'winbonus':20000},
                                             blockHeuristic:{'multiplier':10,'exponent':4,'weight':2},
                                             openHeuristic:{'multiplier':1,'exponent':3,'weight':10}}
        super().__init__(*args,**kwargs,heuristics=heuristics)
        return    

    def save(self):
        with open(self.filepath,'wb') as f: f.write(dumps(self.heuristics))
    
    #Extendables
    def onWin(self,winner):
        self.save()
