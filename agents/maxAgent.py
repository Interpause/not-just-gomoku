from copy import deepcopy
from agents.baseAgent import baseAgent
from random import choice
class maxAgent(baseAgent):
    '''Agent that assumes opponents always play optimally and use that to deeply calculate state rewards.
    
    Attributes:
        depth (int): How many turns into the future to predict.
        dim (float): Decrease in reward the further one goes into the future due to uncertainty.
        salt (float): How much to penalize the agent for letting the opponent make a good move. High salt values make agents try and prevent the opponent from doing well at all times and can appear as "saltiness".
    
    '''

    def __init__(self,*args,depth=1,dim=0.5,salt=1,**kwargs):
        super().__init__(*args,**kwargs)
        self.depth = depth
        self.dim = dim
        self.salt = salt
        return

    #helper functions
    def reflexStateEvaluate(self,state,piece):
        '''Shallow evaluates state reward using action rewards possible.'''

        cur = None
        best = self.intMin
        for space in state.spaces():
            score = self.reflexEvaluate(space,piece=piece,state=state)
            if score > best:
                best = score
                cur = space
            elif self.fequal(score,best):
                cur = choice([space,cur])
        return (cur,best)

    def getOptimal(self,state,piece,curDepth=0):
        '''Recursive function that deeply evaluates state reward over multiple turns.'''

        if curDepth == self.depth: return self.reflexStateEvaluate(state,piece)
        cur = None
        best = self.intMin
        for space in state.spaces():
            score = 0
            score += self.reflexEvaluate(space,piece=piece,state=state)
            if score < best*(1-self.dim): continue
            
            dupe = deepcopy(state)
            dupe.place(piece,space)
            if dupe.full():
                best = score
                cur = space
                break

            others = self.getNextList(piece)
            point_loss = 0
            for n,other in enumerate(others):
                enemy = self.getOptimal(dupe,other,curDepth+1)
                point_loss += self.salt*enemy[1]
                dupe.place(other,enemy[0])
                if dupe.full(): break
            score -= point_loss/(n+1)
            score += self.getOptimal(dupe,piece,curDepth+1)[1]*self.dim
            if score > best:
                best = score
                cur = space
            elif self.fequal(score,best):
                cur = choice([space,cur])
            elif best == self.intMin:
                best = score
                cur = space
        return (cur,best)

    #Extendables
    #getter
    def getMove(self,state=None):
        super().getMove(state=state)
        return self.getOptimal(state,self.piece)[0]
