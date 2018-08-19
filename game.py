from game_exceptions import *
from heuristics import *
import state
class Game():
    
    def __init__(self,height,length,winnum,agents,silent=False):
        self.pieces = ["X","■","□","○","●","▵","▴"]#TODO: think of more. These are fine and can be treated as enums
        self.ordlist = self.pieces[:len(agents)]
        self.state = state.state(height,length,winnum,self.ordlist)
        self.win = False
        self.silent = silent
        self.agents = [agent(self.state,self.pieces[i],self.ordlist) for i,agent in enumerate(agents)] #initializes all the agents

    #main code
    def update(self):
        for agent in self.agents:
            if self.win != False: return
            self.log("\n"*(self.state.height()+3))
            self.log("%s (Piece: %s)'s Turn!!!"%(self.getName(agent),agent.piece))
            self.log(self.state)
            
            #try:
            self.takeTurn(agent)
            #except BaseException as e:
            #    self.log("Something went wrong!")
            #    self.log(e)
            #    self.win = None
                
            self.checkWin()       
        return

    def takeTurn(self,agent):
        done = False
        while(not done):
            try:
                self.updateAgents(agent.piece)
                coord = self.getMove(agent)
                self.state.place(agent.piece,coord)
                done = True
                
                self.log("%s placed %s at (%d,%d)."%(self.getName(agent),agent.piece,coord[0],coord[1]))
                for heuristic in agent.heuristics: self.log("%s's score: %f" % (heuristic.__name__,heuristic(agent.state,agent.piece,coord)))
                
            except OutOfBoundsException: self.log("Those coordinates are out of bounds!")
            except OutOfSpaceException: self.log("The board is full and the game hasnt ended?")
            except SpaceTakenException: self.log("Space is taken!")
            except KeyboardInterrupt:
                if self.onKeyboardInterrupt():
                    return
        return

    def updateAgents(self,piece):
        for other in self.agents:
            start = time.time()
            other.update(self.state,piece)
            end = time.time()
            self.log("%s took %fs to update."%(self.getName(other),end-start))
        return

    def getMove(self,agent):
        start = time.time()
        coord = agent.getMove(self.state)
        end = time.time()
        self.log("%s took %fs to decide."%(self.getName(agent),end-start))
        return coord
    
    def checkWin(self):
        winner = self.state.isWin()
        if winner != True and winner != False:
                for agent in self.agents:
                    if agent.piece == winner:
                        winner = agent
                        break
                print("%s (Piece: %s) wins!!!"%(self.getName(winner),winner.piece))
                self.win = winner.piece
        elif winner == True:
                print("The board is full!!! ITS A DRAW")
                self.win = None
        self.updateAgents(self.win)
        for agent in self.agents: agent.onWin(self.win)
        return
            
    #helper functions
    #KeyboardInterrupt handler
    def onKeyboardInterrupt(self):
        try:
            ans = input("Are you sure you want to quit? (Y)")
        except KeyboardInterrupt:
            return self.onKeyboardInterrupt()
        if ans == 'y' or ans == 'Y':
            print("Game Over!~")
            self.win = None
            return True
        else:
            print("So be it.")
            return False
        return

    def getName(self,obj):
            return type(obj).__name__

    def log(self,msg):
        if self.silent: return
        print(msg)
        return
    
if __name__ == "__main__":
    #Heuristics
        #Cluster Heuristic #Falls under foresight tho. maxAgent naturally spaces weirdly.
            #Determines how to strategically cluster pieces
            #Encourages directing the flow rather than following it
        #Create a set of state heuristics

    #Agents
        #markovAgent
            #only agent to not utilize default/handtuned options for heuristics
            #uses sigmoid network to adjust best weights, score formulae and special case scores
            #needs two set of special options, one for itself and one for its opponent if based on maxAgent
        #extendedMarkovAgent
            #based on markovAgent, but creates multiple competing models to predict opponents playstyle
        #expectiAgent
            #maxAgent but non-prioritising
            #^figure out how to prevent expectiAgent from being ungodly slow
        #maxThreadedAgent
            #fix one day


    from agents.guiPlayerAgent import guiPlayerAgent as player
    from agents.simpleAgent import simpleAgent as sim
    from agents.markovSimpleAgent import markovSimpleAgent as simM
    from agents.maxThreadedAgent import maxThreadedAgent as maxy
    from agents.maxAgent import maxAgent as maxx
    from agents.baseAgent import baseAgent as whywouldyou
    import time
    from threading import Thread
    
    #AI2.maxAgent
    #AI.simpleAgent
    #player.playerAgent
        
    while(True):
        start = time.time()
        main = Game(10,10,5,[maxx,sim,player],silent = False)
        done = False
        def autorestart():
            loops = 0
            while not done:
                time.sleep(5)
                loops+=1
                if loops==36000:
                    main.win = None
                    break
        while(main.win==False):
            done = False
            Thread(target=autorestart).start()
            main.update()
            done = True
        end = time.time()
        print(end - start)
