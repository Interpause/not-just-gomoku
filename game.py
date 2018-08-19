from game_exceptions import *
from heuristics import *
class Game():

    def onKeyboardInterrupt(self):
        ans = input("Are you sure you want to quit? (Y)")
        if ans == 'y' or ans == 'Y':
            print("Game Over!~")
            return True
        return False
    
    def __init__(self,height,length,winnum,agents,silent=False):
        import state
        self.pieces = ["X","■","□","○","●","▵","▴"]#TODO: think of more
        self.state = state.state(height,length,winnum,self.pieces[:len(agents)])
        win = False
        while(not win):
            for i, agent in enumerate(agents):
                try:
                    if not silent:
                        print("\n"*(height+3))
                        print("%s (Piece: %s, ID: %d)'s Turn!!!"%(agent.__name__,self.pieces[i],i))
                        print(self.state)
                    done = False
                except KeyboardInterrupt:
                    if onKeyboardInterrupt():
                        return
                    else:
                        i-=1
                        continue
                while(not done):
                    try:
                        coord = agent(self.state,self.pieces[i],self.pieces[:len(agents)])
                        self.state.place(self.pieces[i],coord)
                        done = True
                        if not silent:
                            print("%s placed %s at (%d,%d)."%(agent.__name__,self.pieces[i],coord[0],coord[1]))
                            #print(lineHeuristic(self.state,self.pieces[i],coord))
                            #print(blockHeuristic(self.state,self.pieces[i],coord))
                    except KeyboardInterrupt:
                        if self.onKeyboardInterrupt():
                            return
                    except OutOfBoundsException:
                        if not silent:
                            print("Those coordinates are out of bounds!")
                    except OutOfSpaceException:
                        if not silent:
                            print("The board is full and the game hasnt ended?")
                    except SpaceTakenException:
                        if not silent:
                            print("Space is taken!")
                    except BaseException as e:
                        if not silent:
                            print("Something went wrong!")
                        print(e)
                        return
                winner = self.state.isWin()
                if winner != True and winner != False:
                    print("%s (Piece: %s, ID: %d) wins!!!"%(agents[self.pieces.index(winner)].__name__,winner,self.pieces.index(winner)))
                    win = True
                    self.win = winner
                    return
                if winner == True:
                    print("The board is full!!! ITS A DRAW")
                    win = True
                    return                  
                              
if __name__ == "__main__":
    import agents.playerAgent as player
    import agents.guiPlayerAgent as P
    import agents.simpleAgent as AI
    import agents.maxAgent as AI2
    import time
    #AI2.maxAgent
    #AI.simpleAgent
    #player.playerAgent
    #a = Game(5,5,5,[player.playerAgent,player.playerAgent])

    #Heuristics
        #Template and inherit heuristics
        #Generally split heuristics into functions for less repetition
        #Create keyword options
            #custom score formula
            #specify absolute or relative values of special cases (win, lose, danger, etc)
            #specify weight
        #Absolutes shouldnt immediately return.
            #what if the agents start going for scenarios that allow them 5 wins at once?
            #r/hmm
        #Block Heuristic
            #Anything less than 5 is buggy
            #Figure out why maxAgent prefers blocking opportunities to blocking
            #Maybe give score based on proximity to actual chain?
            #maybe try making a new block heuristic from scratch
            #Double check it actually checks both sides are sealed
            #seems aggressive about blocking (i amped the defaults) but gives up past a point???
            #Differentiate between for danger and fatal (might be main problem):
                #OXXXO, XXOXX, XXXXO, XOXXX, XOXXO, XOOXX
            #Seems to love BOXXXOB cause can get lots of block points without doing anything?
        #Cluster Heuristic
            #Determines when piece is too surrounded
            #Determines when good idea to move away from cluster
            #Acts as start piece strategic randomnizer
            #Encourages directing the flow rather than following it
        #Line Heuristic
            #Prefer diagonals, combined with cluster heuristic = good strategy
        #Space Heuristic (may be unused)
            #Broadly assumes which spaces arent worth trying out
        #Create a set of state heuristics
        #Create support for the eventual markovAgent

    #Agents
        #Make agents into classes
            #BaseAgent inheritance
            #Each agent keeps image of state
        #Agent options
            #default handtuned options
            #user specified options
                #e.g. maxAgent's dim, reflexAgent's heuristic settings...
        #markovAgent
            #only agent to not utilize default/handtuned options for heuristics
            #inherits from maxAgent?
            #uses sigmoid network to adjust best weights, score formulae and special case scores
        #expectiAgent
            #maxAgent but non-prioritising
            #^figure out how to prevent expectiAgent from being ungodly slow
        #MaxAgent
            #Factor in reducing opponent's state utility (can be done at simulation part)
            #Does 1 - dim filtering block out special case absolute scores?
                #hmm it seems to work like some sort of difficulty control.
                #broken blockHeuristic still messing things up though
                    #makes maxAgents prediction of optimal move off
            #Main weakness: opponents not playing optimally
                #yet the reflex agent is suffering the same dont block just wait glitch?
        #Use flagging for agents
            #Agents can effectively be own threads now.

    #Game
        #Update each agent's state each turn
        #Use flagging for agents
    
    while(True):
        player = P.guiPlayerAgent(10,10)
        start = time.time()
        a = Game(10,10,5,[player.getMove,AI.simpleAgent],silent = False)
        end = time.time()
        print(end - start)
