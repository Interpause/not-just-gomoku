from copy import deepcopy
from collections import OrderedDict
from agents.baseThreadedAgent import baseThreadedAgent
#contains expectimax like elements. might actually be expectimax.
#screwedover
class maxThreadedAgent(baseThreadedAgent):

    def __init__(self,*args,depth=1,dim=0.5,salt=1,scenarios=5,**kwargs):
        super().__init__(*args,**kwargs)
        self.depth = depth
        self.dim = 0.5
        self.salt = 1
        self.scenarios = scenarios
        return
    
    #Override
    def calculate(self):
        if self.curPiece == self.piece:
            for key,value in self.expected.items():
                if value == self.state.grid():
                    self.move = key
                    self.expected = {}
                    return
            self.move = list(self.getOptimal(self.state,self.piece).items())[0][0]
            self.expected = {}
        else:
            piece = self.curPiece
            tree = [self.state]
            while(piece!=self.piece):
                if self.isStopping: break
                ntree = []
                for leaf in tree:
                    if self.isStopping: break
                    predicted = self.getOptimal(leaf,self.curPiece)
                    for key,value in predicted.items():
                        dupe = deepcopy(leaf)
                        dupe.place(piece,key)
                        ntree.append(dupe)
                tree = ntree
                piece = self.getNextList(piece)[0]
            for leaf in tree:
                self.expected[list(self.getOptimal(leaf,self.piece).items())[0][0]] = leaf.board()
        return

    #helper functions
    def reflexStateEvaluate(self,state,piece):
        cur = OrderedDict()
        for space in state.spaces():
            if self.isStopping: break
            score = self.reflexEvaluate(space,piece=piece,state=state)
            if len(cur) < self.scenarios:
                cur[space] = score
            else:
                minPair = list(cur.items())[0]
                if score > minPair[1]:
                    cur.popitem(minPair[0])
                    cur[space] = score
            cur = OrderedDict(sorted(cur.items(),key=lambda v: v[1]))      
        return cur
    
    def getOptimal(self,state,piece,curDepth=0):
        if curDepth == self.depth: return self.reflexStateEvaluate(state,piece)
        if self.isStopping: return self.reflexStateEvaluate(state,piece)
        cur = OrderedDict({})
        minPair = ((0,0),self.intMin)
        def compareUpdate(coord,score,cur=cur,minPair=minPair):
            if len(cur) < self.scenarios:
                cur[space] = score
            else:
                if score > minPair[1]:
                    cur.popitem(minPair[0])
                    cur[space] = score
            cur = OrderedDict(sorted(cur.items(),key=lambda v: v[1]))
            minPair = list(cur.items())[0]
            return
        
        for space in state.spaces():
            if self.isStopping: break
            score = 0
            score += self.reflexEvaluate(space,piece=piece,state=state)
            if score < minPair[1]*(1-self.dim): continue

            dupe = deepcopy(state)
            dupe.place(piece,space)
            if dupe.full():
                compareUpdate(space,score)
                break

            others = self.getNextList(piece)
            point_loss = 0
            for n,other in enumerate(others):
                enemy = self.getOptimal(dupe,other,curDepth+1)
                point_loss += sum(enemy.values())/len(enemy)*self.salt
                dupe.place(other,list(enemy.items())[0][0])
                if dupe.full(): break
            score -= point_loss/(n+1)

            future = self.getOptimal(dupe,piece,curDepth+1)
            score += sum(future.values())/len(future)*self.dim#iS THiS eXpEcTimAX?
            compareUpdate(space,score)
        return cur      
