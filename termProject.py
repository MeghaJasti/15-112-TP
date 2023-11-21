from cmu_graphics import *

#-----all piece classes-----#
#pawn class, checks if piece moved up/down one
class Pawn:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validMove(self, newRow, newCol):
        if self.col != newCol:
            return False
        if self.color == "white":
            return self.row - 1 == newRow
        if self.color == "black":
            return self.row + 1 == newRow
        return False
    
#rook class, checks if piece moved in a line
class Rook:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validMove(self, newRow, newCol):
        if self.row == newRow and self.col != newCol:
            return True
        if self.row != newRow and self.col == newCol:
            return True
        return False

#knight class, checks if piece moved in an L
class Knight:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
    
    def validMove(self, newRow, newCol):
        for drow in [-2, 2]:
            for dcol in [-1, 1]:
                if self.row + drow == newRow and self.col + dcol == newCol:
                    return True
        for dcol in [-2, 2]:
            for drow in [-1, 1]:
                if self.row + drow == newRow and self.col + dcol == newCol:
                        return True
        return False

#bishop class, checks if piece moved diagonally
class Bishop:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validMove(self, newRow, newCol):
        drow = abs(newRow - self.row)
        dcol = abs(newCol - self.col)
        if drow == dcol: 
            return True
        return False

#king class, checks if piece moved one square
class King:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validMove(self, newRow, newCol):
        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if (drow, dcol) != (0, 0):
                    if self.row + drow == newRow and self.col + dcol == newCol:
                        return True
        return False

#queen class, checks if piece moved in a line or diagonally
class Queen:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def validMove(self, newRow, newCol):
        if self.row == newRow and self.col != newCol:
            return True
        if self.row != newRow and self.col == newCol:
            return True
        drow = abs(newRow - self.row)
        dcol = abs(newCol - self.col)
        if drow == dcol: 
            return True
        return False
    
#-----graphics-----#

def onAppStart(app):
    #create board dimensions
    app.height = 500
    app.width = 500
    #start game
    reset(app)

def reset(app):
    app.currentPlayer = 1
    #white pawns
    pawnw1 = Pawn("white", 6, 0)
    pawnw2 = Pawn("white", 6, 1)
    pawnw3 = Pawn("white", 6, 2)
    pawnw4 = Pawn("white", 6, 3)
    pawnw5 = Pawn("white", 6, 4)
    pawnw6 = Pawn("white", 6, 5)
    pawnw7 = Pawn("white", 6, 6)
    pawnw8 = Pawn("white", 6, 7)
    #other white pieces
    rookw1 = Rook("white", 7, 0)
    knightw1 = Knight("white", 7, 1)
    bishopw1 = Bishop("white", 7, 2)
    queenw = Queen("white", 7, 3)
    kingw = King("white", 7, 4)
    bishopw2 = Bishop("white", 7, 5)
    knightw2 = Knight("white", 7, 6)
    rookw2 = Rook("white", 7, 7)

    #black pawns
    pawnb1 = Pawn("black", 1, 0)
    pawnb2 = Pawn("black", 1, 1)
    pawnb3 = Pawn("black", 1, 2)
    pawnb4 = Pawn("black", 1, 3)
    pawnb5 = Pawn("black", 1, 4)
    pawnb6 = Pawn("black", 1, 5)
    pawnb7 = Pawn("black", 1, 6)
    pawnb8 = Pawn("black", 1, 7)
    #other black pieces
    rookb1 = Rook("black", 0, 0)
    knightb1 = Knight("black", 0, 1)
    bishopb1 = Bishop("black", 0, 2)
    queenb = Queen("black", 0, 3)
    kingb = King("black", 0, 4)
    bishopb2 = Bishop("black", 0, 5)
    knightb2 = Knight("black", 0, 6)
    rookb2 = Rook("black", 0, 7)

def onKeyPress(app, key):
    if key == "r":
        reset()

def redrawAll(app):
    pass

def main():
    runApp()

main()
