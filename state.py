from copy import deepcopy
from game_exceptions import *
from itertools import product

#TODO: make setters raise errors regarding whether move was successful

class state():
    def __init__(self,height,length,winnum,pieces):
        self.__winnum = winnum
        self.__height = height
        self.__length = length
        self.__pieces = pieces
        self.__empty = list(product(range(length),range(height)))
        self.__board = dict([(piece,[]) for piece in pieces])
        self.__grid = [[None for x in range(length)] for y in range(height)]

    def forgetmefornow(self,memo):
        cls = self.__class__
        
        self.__winnum = other.winnum()
        self.__height = other.height()
        self.__length = other.length()
        self.__pieces = other.pieces()
        self.__empty = other.spaces()
        self.__board = other.board()
        self.__grid = other.grid()
    
    def __str__(self):
        msg = ""
        msg += "Pieces are: %s"%str(self.__pieces).strip('[]')
        msg += "\n"
        msg += ("*-"*self.__length+"*")
        for y in range(self.__height):
            row = ""
            for x in range(self.__length):
                for piece, coords in self.__board.items():
                    if (x,y) in coords:
                        row += ("|"+piece)
                        break
                else:
                    row += "| "
            msg += ("\n"+row+"|")
            msg += ("\n"+"*-"*self.__length+"*")
        msg += ("\nSpaces left: %d"%len(self.__empty))
        msg += ("\nWin condition: %d"%self.__winnum)
        return msg
    
    #Helper functions
    def isEmpty(self,coord):
        if coord[0] < 0 or coord[1] < 0 or coord[0] >= self.__length or coord[1] >= self.__height:
            raise OutOfBoundsException("Coordinates (%d,%d) are out of range of a (%d,%d) board."%(coord+(self.__length,self.__height)))
        if self.__grid[coord[1]][coord[0]] == None:
            return True
        else:
            return False

    def isWin(self):
        for piece,coords in self.__board.items():
            if len(coords) < self.__winnum:
                continue
            else:
                for coord in coords:

                    #TODO: find way to limit coords to those with potential
                    
                    #check horizontal
                    won = True
                    for i in range(self.__winnum):
                        x = coord[0]+i
                        y = coord[1]
                        if x >= self.__length:
                            won = False
                            break
                        if self.__grid[y][x] != piece:
                            won = False
                            break
                    if won:
                        return piece

                    #check vertical
                    won = True
                    for i in range(self.__winnum):
                        x = coord[0]
                        y = coord[1]+i
                        if y >= self.__height:
                            won = False
                            break
                        if self.__grid[y][x] != piece:
                            won = False
                            break
                    if won:
                        return piece

                    #check right diagonal
                    won = True
                    for i in range(self.__winnum):
                        x = coord[0]+i
                        y = coord[1]+i
                        if x >= self.__length or y >= self.__height:
                            won = False
                            break
                        if self.__grid[y][x] != piece:
                            won = False
                            break
                    if won:
                        return piece

                    #check left diagonal
                    won = True
                    for i in range(self.__winnum):
                        x = coord[0]+i
                        y = coord[1]-i
                        if x >= self.__length or y < 0:
                            won = False
                            break
                        if self.__grid[y][x] != piece:
                            won = False
                            break
                    if won:
                        return piece
        if len(self.__empty) == 0:
            return True
        return False
    
    #safe getters
    def board(self):
        return deepcopy(self.__board)
    def grid(self):
        return deepcopy(self.__grid)
    def height(self):
        return int(self.__height)
    def length(self):
        return int(self.__length)
    def winnum(self):
        return int(self.__winnum)
    def pieces(self):
        return list(self.__pieces)
    def full(self):
        return len(self.__empty) == 0
    def spaces(self):
        return list(self.__empty)
    
    #unsafe setters
    def overwrite(self,piece,coord):
        self.erase(coord)
        self.__board[piece].append(coord)
        self.__empty.remove(coord)
        self.__grid[coord[1]][coord[0]] = piece
        return

    def erase(self,coord):
        self.__grid[coord[1]][coord[0]] = None
        for piece in self.__board.values():
            try:
                piece.remove(coord)
                self.__empty.append(coord)
                return
            except ValueError:
                continue
        return

    #all in one function
    def place(self,piece,coord):
        if len(self.__empty) == 0:
            raise OutOfSpaceException("The board is out of space. isWin() should be called.")
        if self.isEmpty(coord):
            self.__board[piece].append(coord)
            self.__empty.remove(coord)
            self.__grid[coord[1]][coord[0]] = piece
        else:
            raise SpaceTakenException("(%d,%d) is taken already."%coord)
        return    

    
if __name__ == "__main__":
    def test():
        print("Simple functionality Test")
        import random
        import string
        h = random.randint(3,10)
        l = random.randint(3,10)
        w = random.randint(3,min(h,l))
        p = random.randint(2,8)
        print("Creating disboard of height %d, length %d, win number of %d and %d pieces..."%(h,l,w,p))
        disboard = state(h,l,w,random.sample(string.ascii_lowercase,p))
        print("Checking pretty print...")
        print(disboard)
        p1 = (random.randint(0,l-1),random.randint(0,h-1))
        c1 = random.choice(disboard.pieces())
        print("Placing %s at random point x=%d, y=%d..." % ((c1,)+p1))
        disboard.place(c1,p1)
        print(disboard)
        l2 = disboard.pieces()
        l2.remove(c1)
        c3 = random.choice(l2)
        print("Placing %s at same point x=%d, y=%d..." % ((c3,)+p1))
        disboard.place(c3,p1)
        print(disboard)
        l1 = disboard.pieces()
        l1.remove(c3)
        c4 = random.choice(l1)
        print("Overwriting with %s at previous point x=%d, y=%d..." % ((c4,)+p1))
        disboard.overwrite(c4,p1)
        print(disboard)
        p2 = (random.randint(0,l-1),random.randint(0,h-1))
        c2 = random.choice(disboard.pieces())
        print("Overwriting with %s at random point x=%d, y=%d..." % ((c2,)+p2))
        disboard.overwrite(c2,p2)
        print(disboard)
        print("Updating spaces left...")
        disboard.update_space()
        print(disboard)
        print("Erasing previous point x=%d, y=%d..." % p1)
        disboard.erase(p1)
        print(disboard)
        p3 = (random.randint(0,l-1),random.randint(0,h-1))
        print("Erasing random point x=%d, y=%d..." % p3)
        disboard.erase(p3)
        print(disboard)
        print("Updating spaces left...")
        disboard.update_space()
        print(disboard)
        print("Testing if erased point is empty...")
        print(disboard.isEmpty(p1))
        print("Testing if previous point is empty...")
        print(disboard.isEmpty(p2))
        print("\nWin function Test")
        for i in range(10):
            h = random.randint(3,10)
            l = random.randint(3,10)
            w = random.randint(3,min(h,l))
            p = random.randint(2,8)
            disboard = state(h,l,w,random.sample(string.ascii_lowercase,p))
            prev = disboard.pieces()[0]
            for y in range(h):
                for x in range(l):
                    playable = disboard.pieces()
                    playable.remove(prev)
                    prev = random.choice(playable)
                    disboard.place(prev,(x,y))
                    if disboard.isWin() != False:
                        break
                else:
                    continue
                break
            if disboard.isWin() == True:
                print(disboard)
                print("DRAW!")
            else:
                print(disboard)
                print("%s WINS!"%disboard.isWin())
            
    test()
