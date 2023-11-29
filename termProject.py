from cmu_graphics import *

#-----all piece classes-----#
#pawn class, checks if piece moved up/down one
class Pawn:
    def __init__(self, color, row, col, turn):
        self.color = color
        self.row = row
        self.col = col
        self.turn = turn
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white pawn.png"
        else:
            self.image = "chess pieces/black pawn.png"

    def validMove(self, newRow, newCol, board):
        if self.col != newCol:
            print("horizontal")
            return False
        if self.turn == 0:
            if self.color == "white" and (self.row - 1 == newRow or self.row - 2 == newRow):
                self.turn += 1
                return True
            if self.color == "black" and (self.row + 1 == newRow or self.row + 2 == newRow):
                self.turn += 1
                return True
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
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white rook.png"
        else:
            self.image = "chess pieces/black rook.png"

    def validMove(self, newRow, newCol, board):
        if self.row == newRow and self.col != newCol:
            return self.noObstaclesLine(newRow, newCol, board)
        if self.row != newRow and self.col == newCol:
            return self.noObstaclesLine(newRow, newCol, board)
        return False
    
    def noObstaclesLine(self, newRow, newCol, board):
        if self.row == newRow and self.col != newCol:
            if self.col < newCol:
                lower = self.col + 1
                upper = newCol
            else:
                upper = self.col
                lower = newCol + 1
            for col in range(lower, upper):
                if board[self.row][col] != "-":
                    return False
        elif self.row != newRow and self.col == newCol:
            if self.row < newRow:
                lower = self.row + 1
                upper = newRow
            else:
                upper = self.row
                lower = newRow + 1
            for row in range(lower, upper):
                if board[row][self.col] != "-":
                    return False
        return True

#knight class, checks if piece moved in an L
class Knight:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white knight.png"
        else:
            self.image = "chess pieces/black knight.png"
    
    def validMove(self, newRow, newCol, board):
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
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white bishop.png"
        else:
            self.image = "chess pieces/black bishop.png"

    def validMove(self, newRow, newCol, board):
        dRow = abs(newRow - self.row)
        dCol = abs(newCol - self.col)
        if dRow == dCol: 
            return self.noObstaclesDiagonal(newRow, newCol, board)
        return False
    
    def noObstaclesDiagonal(self, newRow, newCol, board):
        if newRow - self.row < 0:
            dRow = -1
        else:
            dRow = 1
        if newCol - self.col < 0:
            dCol = -1
        else:
            dCol = 1
        for dif in range(1, abs(newRow - self.row)):
            print(self.row + dRow * dif, self.col + dCol * dif)
            if board[self.row + dRow * dif][self.col + dCol * dif] != "-":
                return False
        return True

#king class, checks if piece moved one square
class King:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white king.png"
        else:
            self.image = "chess pieces/black king.png"

    def validMove(self, newRow, newCol, board):
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
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white queen.png"
        else:
            self.image = "chess pieces/black queen.png"

    def validMove(self, newRow, newCol, board):
        if self.row == newRow and self.col != newCol:
            return self.noObstaclesLine(newRow, newCol, board)
        if self.row != newRow and self.col == newCol:
            return self.noObstaclesLine(newRow, newCol, board)
        drow = abs(newRow - self.row)
        dcol = abs(newCol - self.col)
        if drow == dcol: 
            return self.noObstaclesDiagonal(newRow, newCol, board)
        return False
    
    def noObstaclesLine(self, newRow, newCol, board):
        if self.row == newRow and self.col != newCol:
            if self.col < newCol:
                lower = self.col + 1
                upper = newCol
            else:
                upper = self.col
                lower = newCol + 1
            for col in range(lower, upper):
                if board[self.row][col] != "-":
                    return False
        elif self.row != newRow and self.col == newCol:
            if self.row < newRow:
                lower = self.row + 1
                upper = newRow
            else:
                upper = self.row
                lower = newRow + 1
            for row in range(lower, upper):
                if board[row][self.col] != "-":
                    return False
        return True
    
    def noObstaclesDiagonal(self, newRow, newCol, board):
        if newRow - self.row < 0:
            dRow = -1
        else:
            dRow = 1
        if newCol - self.col < 0:
            dCol = -1
        else:
            dCol = 1
        for dif in range(1, abs(newRow - self.row)):
            print(self.row + dRow * dif, self.col + dCol * dif)
            if board[self.row + dRow * dif][self.col + dCol * dif] != "-":
                return False
        return True
    
#-----graphics-----#

def onAppStart(app):
    #create board dimensions
    app.height = 500
    app.width = 500
    #start game
    reset(app)

#restart the game
def reset(app):
    app.currentPlayer = "White"
    app.beginMove = None
    app.endMove = None
    app.message = None
    #white pawns
    app.pawnw1 = Pawn("white", 6, 0, 0)
    app.pawnw2 = Pawn("white", 6, 1, 0)
    app.pawnw3 = Pawn("white", 6, 2, 0)
    app.pawnw4 = Pawn("white", 6, 3, 0)
    app.pawnw5 = Pawn("white", 6, 4, 0)
    app.pawnw6 = Pawn("white", 6, 5, 0)
    app.pawnw7 = Pawn("white", 6, 6, 0)
    app.pawnw8 = Pawn("white", 6, 7, 0)
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
    app.pawnb1 = Pawn("black", 1, 0, 0)
    app.pawnb2 = Pawn("black", 1, 1, 0)
    app.pawnb3 = Pawn("black", 1, 2, 0)
    app.pawnb4 = Pawn("black", 1, 3, 0)
    app.pawnb5 = Pawn("black", 1, 4, 0)
    app.pawnb6 = Pawn("black", 1, 5, 0)
    app.pawnb7 = Pawn("black", 1, 6, 0)
    app.pawnb8 = Pawn("black", 1, 7, 0)
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
    app.board = [[app.rookb1, app.knightb1, app.bishopb1, app.queenb, app.kingb, app.bishopb2, app.knightb2, app.rookb2],
                 [app.pawnb1, app.pawnb2, app.pawnb3, app.pawnb4, app.pawnb5, app.pawnb6, app.pawnb7, app.pawnb8], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 ["-", "-", "-", "-", "-", "-", "-", "-"], 
                 [app.pawnw1, app.pawnw2, app.pawnw3, app.pawnw4, app.pawnw5, app.pawnw6, app.pawnw7, app.pawnw8], 
                 [app.rookw1, app.knightw1, app.bishopw1, app.queenw, app.kingw, app.bishopw2, app.knightw2, app.rookw2]
    ]

#reset game if "r" is pressed
def onKeyPress(app, key):
    if key == "r":
        reset(app)

def onMousePress(app, mouseX, mouseY):
    #find location
    row = (mouseY - 50)//50
    col = (mouseX - 50)//50
    #determine if click was the beginning or end of a move
    if app.beginMove == None:
        app.beginMove = [row, col]
        app.message = None
    elif app.beginMove == [row, col]:
        app.beginMove = None
        app.endMove = None
        app.message = None
    else: 
        app.endMove = [row, col]
        makeMove(app)
    
def makeMove(app):
    #find piece and potential captured piece
    piece = app.board[app.beginMove[0]][app.beginMove[1]]
    capturePiece = app.board[app.endMove[0]][app.endMove[1]]
    valid = piece.validMove(app.endMove[0], app.endMove[1], app.board)
    #make move if valid
    if piece.color != app.currentPlayer.lower(): #wrong player
        app.message = "Wrong Player Move!"
    elif capturePiece != "-" and (piece.color == capturePiece.color): #same color pieces
        print("same color")
        app.message = "Invalid Move!"
    elif piece != "-" and valid: #valid move
        print("valid move")
        app.message = ""
        piece.row = app.endMove[0]
        piece.col = app.endMove[1]
        app.board[app.beginMove[0]][app.beginMove[1]] = "-"
        app.board[app.endMove[0]][app.endMove[1]] = piece
        app.beginMove = None
        app.endMove = None
        if piece.color == "white":
            app.currentPlayer = "Black"
        else:
            app.currentPlayer = "White"
    elif not valid: #invalid move
        print("not valid move")
        app.message = "Invalid Move!"

#draw the board
def drawBoard(app):
    height = 400
    cellSize = height/8
    color = "silver"
    for row in range(8):
        for col in range(8):
            #change border color based on selection
            if app.beginMove == [row, col]:
                border = "green"
            elif app.endMove == [row, col]:
                border = "red"
            else:
                border = "black"
            #draw grid
            drawRect(50 + cellSize*col, 50 + cellSize*row, cellSize, cellSize, fill = color, border = border, borderWidth = 2)
            #switch colors
            if color == "silver": color = "dimGray"
            else: color = "silver"
        if color == "silver": color = "dimGray"
        else: color = "silver"
    #draw border
    drawRect(50, 50, 400, 400, fill = None, border = 'black', borderWidth = 4)

#draw pieces
def drawPieces(app):
    height = 400
    cellSize = height/8
    for row in range(8):
        for col in range(8):
            piece = app.board[row][col]
            if piece != "-":
                drawImage(piece.image, 50 + cellSize*col, 50 + cellSize*row, width = cellSize, height = cellSize)

def redrawAll(app):
    #draw board, pieces, and text
    drawBoard(app)
    drawPieces(app)
    if app.message != None:
        drawLabel(app.message, 250, 475, fill = "red", size = 20)
    drawLabel("Current Player: " + app.currentPlayer, 250, 25, size = 20)

def main():
    runApp()

main()
