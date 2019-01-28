# Cooper Parker
# Dr. Lisa Torrey
#
# Homework 1
#
# Tomas Cesped, Taylor Digilio, and I worked on this assignment together, but all
# wrote our own personal code

from solving.utils.framework import Puzzle

SIZE = 5

GRID = [
    "XXXXX",
    "X876X",
    "X254X",
    "X3 1X",
    "XXXXX"
]

GRIDWON = [
    "XXXXX",
    "X123X",
    "X456X",
    "X78 X",
    "XXXXX"
]


class Tiles(Puzzle):

    def __init__(self, row=3, column=2, replacement=""):
        self.row = row
        self.column = column
        self.replacement = ""

    def __eq__(self, other):
        return (self.row, self.column) == (other.row, other.column)

    def __hash__(self):
        return hash(self.row, self.column)

    # Return whether this puzzle is solved
    def solved(self):
        return GRID == GRIDWON

    # Return a list of legal moves
    def moves(self):
        moves = list()
        if GRID[self.row - 1][self.column] != 'X':
            moves.append((-1, 0))
        if GRID[self.row + 1][self.column] != 'X':
            moves.append((1, 0))
        if GRID[self.row][self.column - 1] != 'X':
            moves.append((0, -1))
        if GRID[self.row][self.column + 1] != 'X':
            moves.append((0, 1))
        return moves

    # Return a new puzzle created by a move
    def neighbor(self, move):
        (dr, dc) = move
        new_self = GRID[self.row + dr][self.column + dc]

        line = ""

        for index in GRID[self.row]:
            if index == new_self:
                line += " "
            elif index == " ":
                line += new_self
            else:
                line += index

        line2 = ""

        if self.row != self.row + dr:
            for item in GRID[self.row + dr]:
                if item == new_self:
                    line2 += " "
                else:
                    line2 += item

            GRID[self.row + dr] = line2

        replacement = new_self

        GRID[self.row] = line
        return Tiles(self.row + dr, self.column + dc, replacement)

    # Print this puzzle to the console
    def display(self):
        for r in range(SIZE):
            for c in range(SIZE):
                if (r, c) == (self.row, self.column):
                    print("!", end='')
                else:
                    print(GRID[r][c], end='')
            print()
        print()
