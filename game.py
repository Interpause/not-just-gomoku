class Game():

    def __init__(self,height,length,winno,agents,silent=False):
        import state
        self.pieces = ["X","■","□","○","●","▵","▴"]#TODO: think of more
        self.state = state.state(winno,height,length,self.pieces[:len(agents)])
        win = False
        self.win = self.state.emptypiece
        while(not win):
            for i, agent in enumerate(agents):
                try:
                    if not silent:
                        print("\n"*(height+3))
                        print("%s (Piece: %s, ID: %d)'s Turn!!!"%(agent.__name__,self.pieces[i],i))
                        self.drawBoard()
                    done = False
                except KeyboardInterrupt:
                    ans = input("Are you sure you want to quit? (Y)")
                    if ans == 'y' or ans == 'Y':
                        print("Game Over!~")
                        win = True
                        done = True
                        break
                    else:
                        i-=1
                        continue
                while(not done):
                    try:
                        coord = agent(self.state,self.pieces[i])
                        if self.state.getBoard()[coord[1]][coord[0]] != self.state.emptypiece:
                            if not silent:
                                print("Taken coord! Try Again!")
                        else:
                            done = True
                            self.state.update(coord,self.pieces[i])
                            if not silent:
                                print("%s placed %s at (%d,%d)."%(agent.__name__,self.pieces[i],coord[0],coord[1]))
                    except KeyboardInterrupt:
                        ans = input("Are you sure you want to quit? (Y)")
                        if ans == 'y' or ans == 'Y':
                            print("Game Over!~")
                            win = True
                            done = True
                            break
                    except BaseException as e:
                        if not silent:
                            print("Invalid coord!! Try Again!")
                        print(e)
                if win:
                    break
                winner = self.state.isWin()
                if winner != self.state.emptypiece:
                    print("%s (Piece: %s, ID: %d) wins!!!"%(agents[self.pieces.index(winner)].__name__,winner,self.pieces.index(winner)))
                    win = True
                    self.win = winner
                    break
                if self.state.isFull():
                    print("The board is full!!! ITS A DRAW")
                    win = True
                    break                    
                
    def drawBoard(self):
        board = self.state.getBoard()
        height = len(board)
        length = len(board[0])
        print("*-"*length+"*")
        for y in range(height):
            row = ""
            for x in range(length):
                row += "|%s"%board[y][x]
            print(row+"|")
            print("*-"*length+"*")
                              
if __name__ == "__main__":
    import agents.playerAgent as player
    import agents.simpleAgent as AI
    import agents.minmaxAgent as AI2
    import time
    #AI2.minmaxAgent
    #AI.simpleAgent
    #player.playerAgent
    start = time.time()
    a = Game(10,10,5,[AI.simpleAgent,AI.simpleAgent], silent = True)
    end = time.time()
    print(end - start)
    #a = Game(5,5,3,[AI.simpleAgent,AI.simpleAgent])
