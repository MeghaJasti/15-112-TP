from cmu_graphics import *

class Board:
    #create a blank board
    def __init__(self):
        grid = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
        fill = False
    
    #add a piece to the grid
    def addPiece(self, piece, row, col):
        self.grid[row][col] = piece
    
    #check if a player won a board
    def threeInRow(self, piece):
        #filled row
        filled = [piece, piece, piece]
        #check diagonals
        leftToRightDiagonal = [self.grid[0][0], self.grid[1][1], self.grid[2][2]]
        rightToLeftDiagonal = [self.grid[0][2], self.grid[1][1], self.grid[2][0]]
        if leftToRightDiagonal == filled or rightToLeftDiagonal == filled:
            self.fill = True
            return True
        for i in [0, 1, 2]:
            #check rows
            if self.grid[i] == filled: 
                self.fill = True
                return True
            #check columns
            col = [self.grid[i][0], self.grid[i][1], self.grid[i][2]]
            if col == filled:
                self.fill = True
                return True
    
    #check if the board is full
    def full(self):
        for row in [0, 1, 2]:
            for col in [0, 1, 2]:
                if self.grid[row][col] == "-":
                    return False
        self.fill = True
        return True
    
#graphics

def onAppStart(app):
    pass

def onKeyPress(app, key):
    pass

def redrawAll(app):
    pass

def main():
    runApp()

main()
