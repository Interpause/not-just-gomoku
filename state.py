import copy
class state():
    def __init__(self,winno,height,length,pieces):
        self.winNum = winno
        self.height = height
        self.length = length
        self.pieces = pieces
        self.emptypiece = " "
        self.empty = True
        self.board = [[self.emptypiece for x in range(length)] for y in range(height)]
        
    def getBoard(self):
        return copy.deepcopy(self.board)

    def getPieces(self):
        return copy.deepcopy(self.pieces)
    
    def update(self,coord,piece):
        self.empty = False
        self.board[coord[1]][coord[0]] = piece

    def isEmpty(self):
        return bool(self.empty)

    def isFull(self):
        for y in range(self.height):
            for x in range(self.length):
                if self.board[y][x]==self.emptypiece:
                    return False
                    break
        return True
    
    def isWin(self):
        for y in range(self.height):
            for x in range(self.length):
                piece = self.board[y][x]
                if piece == self.emptypiece:
                    continue
                
                #check hori
                won = True
                for i in range(self.winNum):
                    try:
                        x1 = x+i
                        y1 = y
                        if x1 < 0 or y1 < 0:
                            assert(False)
                        if self.board[y1][x1]!=piece:
                            won = False
                            break
                    except:
                        won = False
                        break
                if won:
                    return piece
                
                #check vert
                won = True
                for i in range(self.winNum):
                    try:
                        x1 = x
                        y1 = y+i
                        if x1 < 0 or y1 < 0:
                            assert(False)
                        if self.board[y1][x1]!=piece:
                            won = False
                            break
                    except:
                        won = False
                        break
                if won:
                    return piece

                #check rightdiag
                won = True
                for i in range(self.winNum):
                    try:
                        x1 = x+i
                        y1 = y+i
                        if x1 < 0 or y1 < 0:
                            assert(False)
                        if self.board[y1][x1]!=piece:
                            won = False
                            break
                    except:
                        won = False
                        break
                if won:
                    return piece

                #check leftdiag
                won = True
                for i in range(self.winNum):
                    try:
                        x1 = x-i
                        y1 = y+i
                        if x1 < 0 or y1 < 0:
                            assert(False)
                        if self.board[y1][x1]!=piece:
                            won = False
                            break
                    except:
                        won = False
                        break
                if won:
                    return piece
        return self.emptypiece
