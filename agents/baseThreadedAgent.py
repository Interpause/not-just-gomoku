from threading import Thread
from time import sleep
from agents.baseAgent import baseAgent

class baseThreadedAgent(baseAgent):
    '''Extends baseAgent in order to provide multithreading functionality.
    
    Attributes:
        thread (Thread): Thread used by agent to do precalculations.
        isStopping (bool): Whether the thread is being interrupted. Should not be set.
        expected (dict): The expected future states and the optimal moves for those states.
        move (tuple): The current move, I think.
    '''

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
        '''How precalculations should be done. Should be overrided.'''

        pass

    #getter
    def getMove(self,state=None):
        super().getMove(state)
        while(self.move == None):
            sleep(5)
        move = tuple(self.move)
        self.move = None
        return move
