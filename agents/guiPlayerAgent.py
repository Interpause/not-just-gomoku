from tkinter import *
from agents.baseAgent import baseAgent
class guiPlayerAgent(baseAgent):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        #Window initialization
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.geometry("600x600")
        self.window.title("5 Line Game V2.2 - guiPlayerAgent")
        self.frame=Frame(self.window)
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)

        #actual extensions
        self.input = None
        self.btns = []
        return        

    #helper functions
    #enables all buttons
    def enable(self):
        for y in range(self.state.length()):
            for x in range(self.state.length()):
                self.btns[y][x].configure(state=NORMAL)
        return

    #disables all buttons
    def disable(self):
        for y in range(self.state.length()):
            for x in range(self.state.length()):
                self.btns[y][x].configure(state=DISABLED)
        return

    #changes/setups button texts
    def btnupdate(self):
        if self.btns == []:
            self.btninit()
        grid = self.state.grid()
        for y in range(self.state.length()):
            for x in range(self.state.length()):
                self.btns[y][x].configure(text=grid[y][x])
        return

    #handler for buttons
    def passInput(self,coord):
        self.input = coord
        return

    #setup buttons in grid and gives them above handler
    def btninit(self):
        for y in range(self.state.length()):
            row = []
            for x in range(self.state.length()):
                btn = Button(self.frame,text=" ",height=1,width=1,command=lambda coord=(x,y): self.passInput(coord))
                btn.grid(column=x, row=y, sticky=N+S+E+W)
                btn.configure(state=DISABLED)
                row.append(btn)
            self.btns.append(row)

        for x in range(self.state.length()):
            Grid.columnconfigure(self.frame, x, weight=1)

        for y in range(self.state.length()):
            Grid.rowconfigure(self.frame, y, weight=1)
        return

    #extendables
    #setter
    def update(self,state,curPiece):
        super().update(state,curPiece)
        self.btnupdate()
        self.window.update()
        return

    #getter
    def getMove(self,state):
        super().getMove(state)
        self.input = None
        self.enable()
        while(self.input == None):
            self.window.update()
        self.disable()
        return self.input
        
    
