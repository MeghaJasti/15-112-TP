from cmu_graphics import *

#-----all piece classes-----#
#pawn class, checks if piece moved up/down one
class Pawn:
    def __init__(self, color, row, col, turn):
        self.color = color
        self.row = row
        self.col = col
        self.turn = turn
        self.enPassant = False
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white pawn.png"
        else:
            self.image = "chess pieces/black pawn.png"

    def validMove(self, newRow, newCol, board):
        if self.turn == 0:
            if self.color == "white" and (self.row - 1 == newRow or self.row - 2 == newRow) and self.col == newCol:
                self.turn += 1
                if self.row - 2 == newRow:
                    self.turn += 1
                return True
            if self.color == "black" and (self.row + 1 == newRow or self.row + 2 == newRow) and self.col == newCol:
                self.turn += 1
                if self.row + 2 == newRow:
                    self.turn += 1
                return True
        elif self.color == "white":
            print(self.validMoveForward(newRow, newCol, board))
            return self.validMoveForward(newRow, newCol, board) or self.validCapture(newRow, newCol, board) or self.validEnPassant(newRow, newCol, board)
        else:
            return self.validMoveForward(newRow, newCol, board) or self.validCapture(newRow, newCol, board) or self.validEnPassant(newRow, newCol, board)
        return False
    
    def validMoveForward(self, newRow, newCol, board):
        if self.color == "white":
            return self.row - 1 == newRow and self.col == newCol and board[newRow][newCol] == "-"
        else:
            return self.row + 1 == newRow and self.col == newCol and board[newRow][newCol] == "-"
    
    def validCapture(self, newRow, newCol, board):
        dRow = abs(newRow - self.row)
        dCol = abs(newCol - self.col)
        capturedPiece = board[newRow][newCol]
        if self.color == "white":
            return (dRow == dCol == 1 and newRow < self.row and capturedPiece != "-")
        else:
            return (dRow == dCol == 1 and newRow > self.row and capturedPiece != "-")
    
    def validEnPassant(self, newRow, newCol, board):
        dRow = abs(newRow - self.row)
        dCol = abs(newCol - self.col)
        capturedPiece = board[newRow - 1][newCol]
        if dRow == dCol == 1 and capturedPiece != "-" and capturedPiece.color != self.color:
            if isinstance(capturedPiece, Pawn) and capturedPiece.turn == 2:
                capturedPiece.enPassant = True
                return True
        return False
    
    def validPawnPromotion(self):
        if self.color == "white":
            return self.row == 0
        else:
            return self.row == 7
        
    def check(self, board):
        if self.color == "white":
            dRow = -1
        else:
            dRow = 1
        for dCol in [-1, 1]:
            if 0 <= dCol <= 7:
                capturedPiece = board[self.row + dRow][self.col + dCol]
                if isinstance(capturedPiece, King) and self.validCapture(self.row + dRow, self.col + dCol, board):
                    return True
        return False

#rook class, checks if piece moved in a line
class Rook:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.turn = 0
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
        self.turn += 1
        return True
    
    def check(self, board):
        for row in range(8):
            if self.validMove(row, self.col, board):
                piece = board[row][self.col]
                if isinstance(piece, King) and piece.color != self.color:
                    return True
        for col in range(8):
            if self.validMove(self.row, col, board):
                piece = board[self.row][col]
                if isinstance(piece, King) and piece.color != self.color:
                    return True
        return False

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
        for dRow in [-2, 2]:
            for dCol in [-1, 1]:
                if self.row + dRow == newRow and self.col + dCol == newCol:
                    return True
        for dCol in [-2, 2]:
            for dRow in [-1, 1]:
                if self.row + dRow == newRow and self.col + dCol == newCol:
                        return True
        return False
    
    def check(self, board):
        for dRow in [-2, 2]:
            for dCol in [-1, -1]:
                newRow = self.row + dRow
                newCol = self.col + dCol
                if 0 <= newRow <= 7 and 0 <= newCol <= 7:
                    piece = board[newRow][newCol]
                    if isinstance(piece, King) and piece.color != self.color:
                        return True
        for dCol in [-2, 2]:
            for dRow in [-1, -1]:
                newRow = self.row + dRow
                newCol = self.col + dCol
                if 0 <= newRow <= 7 and 0 <= newCol <= 7:
                    piece = board[newRow][newCol]
                    if isinstance(piece, King) and piece.color != self.color:
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
            if board[self.row + dRow * dif][self.col + dCol * dif] != "-":
                return False
        return True
    
    def check(self, board):
        for row in range(8):
            for col in range(8):
                if self.validMove(row, col, board):
                    piece = board[row][col]
                    if isinstance(piece, King) and piece.color != self.color:
                        return True
        return False

#king class, checks if piece moved one square
class King:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col
        self.turn = 0
        #image source: https://clipart-library.com/clip-art/chess-pieces-silhouette-14.htm
        if color == "white":
            self.image = "chess pieces/white king.png"
        else:
            self.image = "chess pieces/black king.png"

    def validMove(self, newRow, newCol, board):
        for drow in [-1, 0, 1]:
            for dcol in [-1, 0, 1]:
                if (drow, dcol) != (0, 0):
                    row = self.row + drow
                    col = self.col + dcol
                    if 0 <= row <= 7 and 0 <= col <= 7:
                        piece = board[self.row + drow][self.col + dcol]
                        if self.row + drow == newRow and self.col + dcol == newCol:
                            if piece == "-" or piece != "-" and piece.color != self.color:
                                self.turn += 1
                                return True
        return False
    
    def check(self, board):
        for row in range(8):
            for col in range(8):
                piece = board[row][col]
                if piece != "-" and piece.color != self.color and piece.validMove(self.row, self.col, board):
                    return True
        return False
    
    def checkmate(self, board):
        validMoves = []
        for dRow in [-1, 0, 1]:
            for dCol in [-1, 0, 1]:
                newRow = self.row + dRow
                newCol = self.col + dCol
                if 0 <= newRow <= 7 and 0 <= newCol <= 7:
                    piece = board[newRow][newCol]
                    if piece == "-" or piece.color != self.color:
                        validMoves.append((newRow, newCol))
        if validMoves == []:
            return False
        for newRow, newCol in validMoves:
            oldRow = self.row
            oldCol = self.col
            self.row = newRow
            self.col = newCol
            if self.check(board) == False:
                self.row = oldRow
                self.col = oldCol
                return False
        self.row = oldRow
        self.col = oldCol
        return True

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
        dRow = abs(newRow - self.row)
        dCol = abs(newCol - self.col)
        if dRow == dCol: 
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
            if board[self.row + dRow * dif][self.col + dCol * dif] != "-":
                return False
        return True
    
    def check(self, board):
        #if there is a check vertically
        for row in range(8):
            if self.validMove(row, self.col, board):
                piece = board[row][self.col]
                if isinstance(piece, King) and piece.color != self.color:
                    return True
        #if there is a check horizontally
        for col in range(8):
            if self.validMove(self.row, col, board):
                piece = board[self.row][col]
                if isinstance(piece, King) and piece.color != self.color:
                    return True
        #if there is a check diagonally
        for row in range(8):
            for col in range(8):
                if self.validMove(row, col, board):
                    piece = board[row][col]
                    if isinstance(piece, King) and piece.color != self.color:
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
    app.currentPlayer = "White"
    app.beginMove = None
    app.endMove = None
    app.message = None
    app.pawnPromotion = None
    app.instructions = False
    app.gameOver = False
    app.check = False
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
    if key == "p":
        reset(app)
    elif key == "c":
        castleQueenSide(app)
    elif key == "d":
        castleKingSide(app)
    elif not app.gameOver:
        app.pawnPromotion = key

def onMousePress(app, mouseX, mouseY):
    #find location
    row = (mouseY - 50)//50
    col = (mouseX - 50)//50
    #show instructions screen
    if 410 <= mouseX <= 490 and 10 <= mouseY <= 40:
        app.instructions = not app.instructions
    #determine if click was the beginning or end of a move
    if 50 <= mouseX <= 450 and 50 <= mouseY <= 450:
        if not app.gameOver:
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
    #make move if valid
    if piece == "-":
        app.message = "Select a piece to move."
    elif piece.color != app.currentPlayer.lower(): #wrong player
        app.message = "Wrong Player Move!"
    elif capturePiece != "-" and (piece.color == capturePiece.color): #same color pieces
        print("same color")
        app.message = "Invalid Move!"
    elif piece != "-" and piece.validMove(app.endMove[0], app.endMove[1], app.board): #valid move
        if app.message != "Check!":
            app.message = None
        piece.row = app.endMove[0]
        piece.col = app.endMove[1]
        app.board[app.beginMove[0]][app.beginMove[1]] = "-"
        app.board[app.endMove[0]][app.endMove[1]] = piece
        app.beginMove = None
        app.endMove = None
        app.check = False
        if isinstance(piece, Pawn) and piece.validPawnPromotion():
            pawnPromotion(app, piece)
        if isinstance(piece, Pawn):
            enPassant(app)
        if piece.check(app.board):
            app.message = "Check!"
            app.check = True
            whiteCheckMate = app.kingw.checkmate(app.board)
            blackCheckMate = app.kingb.checkmate(app.board)
            print(whiteCheckMate, blackCheckMate)
            if whiteCheckMate or blackCheckMate:
                app.message = "Checkmate! Game over."
                app.gameOver = True
        if piece.color == "white":
            app.currentPlayer = "Black"
        else:
            app.currentPlayer = "White"
    else: #invalid move
        print("not valid move")
        app.message = "Invalid Move!"

def pawnPromotion(app, piece):
    row = piece.row
    col = piece.col
    color = piece.color
    if app.pawnPromotion == "r":
        app.pawnPromotion = None
        app.board[row][col] = Rook(color, row, col)
    elif app.pawnPromotion == "k":
        app.pawnPromotion = None
        app.board[row][col] = Knight(color, row, col)
    elif app.pawnPromotion == "b":
        app.pawnPromotion = None
        app.board[row][col] = Bishop(color, row, col)
    elif app.pawnPromotion == "q":
        app.pawnPromotion = None
        app.board[row][col] = Queen(color, row, col)
    else:
        app.message = "Invalid Pawn Promotion!"

def enPassant(app):
    for row in range(8):
        for col in range(8):
            piece = app.board[row][col]
            if piece != "-" and isinstance(piece, Pawn) and piece.enPassant:
                app.board[row][col] = "-"

def castleKingSide(app):
    if not app.check:
        app.message = ""
        if app.currentPlayer == "White":
            if app.board[7][7] == app.rookw2 and app.board[7][4] == app.kingw and app.rookw2.turn == 0 and app.kingw.turn == 0:
                if app.board[7][5] == app.board[7][6] == "-":
                    app.board[7][6] = app.kingw
                    app.board[7][5] = app.rookw2
                    app.board[7][7] = "-"
                    app.board[7][4] = "-"
                    app.kingw.col = 6
                    app.rookw2.col = 5
                    app.kingw.turn += 1
                    app.rookw2.turn += 1
                    app.currentPlayer = "Black"
                else:
                    app.message = "Invalid Castle!"
            else:
                app.message = "Invalid Castle!"
        elif app.currentPlayer == "Black":
            if app.board[0][7] == app.rookb2 and app.board[0][4] == app.kingb and app.rookb2.turn == 0 and app.kingb.turn == 0:
                if app.board[0][5] == app.board[0][6] == "-":
                    app.board[0][6] = app.kingb
                    app.board[0][5] = app.rookb2
                    app.board[0][7] = "-"
                    app.board[0][4] = "-"
                    app.kingb.col = 6
                    app.rookb2.col = 5
                    app.kingb.turn += 1
                    app.rookb2.turn += 1
                    app.currentPlayer = "White"
                else:
                    app.message = "Invalid Castle!"
            else:
                app.message = "Invalid Castle!"
    else:
        app.message = "Invalid Castle!"

def castleQueenSide(app):
    if not app.check:
        app.message = ""
        if app.currentPlayer == "White":
            if app.board[7][0] == app.rookw1 and app.board[7][4] == app.kingw and app.rookw1.turn == 0 and app.kingw.turn == 0:
                if app.board[7][1] == app.board[7][2] == app.board[7][3]== "-":
                    app.board[7][2] = app.kingw
                    app.board[7][3] = app.rookw1
                    app.board[7][0] = "-"
                    app.board[7][4] = "-"
                    app.kingw.col = 2
                    app.rookw1.col = 3
                    app.kingw.turn += 1
                    app.rookw1.turn += 1
                    app.currentPlayer = "Black"
                else:
                    app.message = "Invalid Castle!"
            else:
                app.message = "Invalid Castle!"
        elif app.currentPlayer == "Black":
            if app.board[0][0] == app.rookb1 and app.board[0][4] == app.kingb and app.rookb1.turn == 0 and app.kingb.turn == 0:
                if app.board[0][1] == app.board[0][2] == app.board[0][3] == "-":
                    app.board[0][2] = app.kingb
                    app.board[0][3] = app.rookb1
                    app.board[0][0] = "-"
                    app.board[0][4] = "-"
                    app.kingb.col = 2
                    app.rookb1.col = 3
                    app.kingb.turn += 1
                    app.rookb1.turn += 1
                    app.currentPlayer = "White"
                else:
                    app.message = "Invalid Castle!"
            else:
                app.message = "Invalid Castle!"
    else:
        app.message = "Invalid Castle!"

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

#draw instructions screen
def drawInstructions(app):
    drawLabel("Instructions: ", 250, 25, size = 20, align = "center")

#draw instructions box
def drawInstructionBox(app):
    drawRect(450, 25, 80, 30, fill = "green", align = "center")
    drawLabel("Instructions", 450, 25, align = "center")

def redrawAll(app):
    drawInstructionBox(app)
    if app.instructions:
        drawInstructions(app)
    else:
        #draw board, pieces, and text
        drawBoard(app)
        drawPieces(app)
        if app.message != None:
            drawLabel(app.message, 250, 475, fill = "red", size = 20)
        drawLabel("Current Player: " + app.currentPlayer, 250, 25, size = 20)

def main():
    runApp()

main()
