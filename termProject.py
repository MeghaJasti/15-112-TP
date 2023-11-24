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

#restart the game
def reset(app):
    app.currentPlayer = 1
    app.beginMove = None
    app.endMove = None
    #white pawns
    app.pawnw1 = Pawn("white", 6, 0)
    app.pawnw2 = Pawn("white", 6, 1)
    app.pawnw3 = Pawn("white", 6, 2)
    app.pawnw4 = Pawn("white", 6, 3)
    app.pawnw5 = Pawn("white", 6, 4)
    app.pawnw6 = Pawn("white", 6, 5)
    app.pawnw7 = Pawn("white", 6, 6)
    app.pawnw8 = Pawn("white", 6, 7)
    #other white pieces
    app.rookw1 = Rook("white", 7, 0)
    app.knightw1 = Knight("white", 7, 1)
    app.bishopw1 = Bishop("white", 7, 2)
    app.queenw = Queen("white", 7, 3)
    app.kingw = King("white", 7, 4)
    app.bishopw2 = Bishop("white", 7, 5)
    app.knightw2 = Knight("white", 7, 6)
    app.rookw2 = Rook("white", 7, 7)

    #black pawns
    app.pawnb1 = Pawn("black", 1, 0)
    app.pawnb2 = Pawn("black", 1, 1)
    app.pawnb3 = Pawn("black", 1, 2)
    app.pawnb4 = Pawn("black", 1, 3)
    app.pawnb5 = Pawn("black", 1, 4)
    app.pawnb6 = Pawn("black", 1, 5)
    app.pawnb7 = Pawn("black", 1, 6)
    app.pawnb8 = Pawn("black", 1, 7)
    #other black pieces
    app.rookb1 = Rook("black", 0, 0)
    app.knightb1 = Knight("black", 0, 1)
    app.bishopb1 = Bishop("black", 0, 2)
    app.queenb = Queen("black", 0, 3)
    app.kingb = King("black", 0, 4)
    app.bishopb2 = Bishop("black", 0, 5)
    app.knightb2 = Knight("black", 0, 6)
    app.rookb2 = Rook("black", 0, 7)

    #initialize board
    app.board = [[app.rookb1, app.knightb1, app.bishopb2, app.queenb, app.kingb, app.bishopb2, app.knightb2, app.rookb2],
                 [app.pawnb1, app.pawnb2, app.pawnb3, app.pawnb4, app.pawnb5, app.pawnb6, app.pawnb7, app.pawnb8], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 [app.pawnw1, app.pawnw2, app.pawnw3, app.pawnw4, app.pawnw5, app.pawnw6, app.pawnw7, app.pawnw8], 
                 [app.rookw1, app.knightw1, app.bishopw2, app.queenw, app.kingw, app.bishopw2, app.knightw2, app.rookw2]
    ]

#reset game if "r" is pressed
def onKeyPress(app, key):
    if key == "r":
        reset()

def onMousePress(app, mouseX, mouseY):
    row = (mouseX - 50)//50
    col = (mouseY - 50)//50

#draw the board
def drawBoard(app):
    height = 400
    cellSize = height/8
    color = "silver"
    for row in range(8):
        for col in range(8):
            #draw grid
            drawRect(50 + cellSize*row, 50 + cellSize*col, cellSize, cellSize, fill = color, border='black', borderWidth = 2)
            #switch colors
            if color == "silver": color = "dimGray"
            else: color = "silver"
        if color == "silver": color = "dimGray"
        else: color = "silver"
    #draw border
    drawRect(50, 50, 400, 400, fill = None, border = 'black', borderWidth = 4)
    
def redrawAll(app):
    #current player
    if app.currentPlayer == 1:
        currentPlayer = "White"
    else:
        currentPlayer = "Black"
    drawLabel("Current Player: " + currentPlayer, 250, 25, size = 20)
    #draw board
    drawBoard(app)

def main():
    runApp()

main()
