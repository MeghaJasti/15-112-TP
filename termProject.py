from cmu_graphics import *

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
