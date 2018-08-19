from threading import Thread
from time import sleep
from agents.baseAgent import baseAgent
class baseThreadedAgent(baseAgent):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.thread = None
        self.isStopping = False
        self.expected = {} #state and move pairs
        self.move = None

    #Extendables
    #setter
    def update(self,state,curPiece):
        super().update(state,curPiece)
        if self.thread != None:
            self.isStopping = True
            self.thread.join()
            self.thread = None
        self.isStopping = False
        self.thread = Thread(target = self.calculate())
        self.thread.start()
        return        

    #for classes to implement
    def calculate(self):
        pass

    #getter
    def getMove(self,state=None):
        super().getMove(state)
        while(self.move == None):
            sleep(5)
        move = tuple(self.move)
        self.move = None
        return move
