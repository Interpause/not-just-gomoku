from tkinter import *
class guiPlayerAgent():

    def __init__(self,height,length):
        self.window = Tk()
        self.window.resizable(0,0)
        self.window.geometry("600x600")
        self.title = "5 Line Game V2 - guiPlayerAgent"
        self.frame=Frame(self.window)
        Grid.rowconfigure(self.window, 0, weight=1)
        Grid.columnconfigure(self.window, 0, weight=1)
        self.frame.grid(row=0, column=0, sticky=N+S+E+W)
        
        self.input = None
        Grid.rowconfigure(self.frame, 0, weight=1)
        Grid.columnconfigure(self.frame, 0, weight=1)
        
        self.length = length
        self.height = height
        self.btns = []
        
        #example values
        for y in range(self.height):
            row = []
            for x in range(self.length):
                btn = Button(self.frame,text=" ",height=1,width=1,command=lambda coord=(x,y): self.passInput(coord))
                btn.grid(column=x, row=y, sticky=N+S+E+W)
                btn.configure(state=DISABLED)
                row.append(btn)
            self.btns.append(row)

        for x in range(self.length):
          Grid.columnconfigure(self.frame, x, weight=1)

        for y in range(self.height):
          Grid.rowconfigure(self.frame, y, weight=1)

    def enable(self):
        for y in range(self.height):
            for x in range(self.length):
                self.btns[y][x].configure(state=NORMAL)
        
    def disable(self):
        for y in range(self.height):
            for x in range(self.length):
                self.btns[y][x].configure(state=DISABLED)

    def update(self,grid):
        for y in range(self.height):
            for x in range(self.length):
                self.btns[y][x].configure(text=grid[y][x])
    
    def getMove(self,state,piece,ordlist):
        self.input = None
        self.enable()
        self.update(state.grid())
        while(self.input == None):
            self.window.update()
        self.disable()
        return self.input
        
    def passInput(self,coord):
        self.input = coord
