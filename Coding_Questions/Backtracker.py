# Algorithms Practice in Python! :) 2021
from typing import List

#--------------------------------------------------------------------------------------------------
class Backtracking:
# 4) Backtracking: use when "optimal solution", "search every possibility", recursion
    # N-Queens Puzzle: Given a NxN chessboard, place n queens on the board 
    # such that no 2 queens can attack each other.
    def __init__(self) -> None:
        self.solutions = []

    # Returns all distinct solutions, in any order.
    # Solution for n = 4: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    def solveNQueens(self, n: int) -> List[List[str]]:
        chessboard = []
        for row in range(n): # add N rows (strings) to the board
            content = ("." * n)
            chessboard.append(content)
        self.recursiveExplorer(n, chessboard, 0)
        print(self.solutions)
        return self.solutions

    # Explores the board for possible solutions. n x n size of board,
    def recursiveExplorer(self, boardSize: int, curr_board: List[str], row: int):
        valid = self.isValid(boardSize, curr_board)
        if not valid: # fail case, backtrack
            return
        if row < boardSize: # Pick from empty spots
            for spot in range(boardSize):
                if curr_board[row][spot] != "Q" and curr_board[row].count("Q") == 0:
                    self.placeQueen(curr_board, row, spot)
                    self.recursiveExplorer(boardSize, curr_board, row + 1)
                    self.removeQueen(curr_board, row, spot)
        else:
            self.solutions.append(curr_board[:]) # base case (solution found)

    # Places a Queen on the given board at a given row and index
    def placeQueen(self, board: List[str], row: int, placeIndex: int):
        board[row] = board[row][:placeIndex] + "Q" + board[row][placeIndex + 1:]

    # Removes a Queen on the given board at a given row and index
    def removeQueen(self, board: List[str], row: int, placeIndex: int):
        board[row] = board[row][:placeIndex] + "." + board[row][placeIndex + 1:]

    # Returns true if the given board is valid (no conflicting Queens)
    def isValid(self, boardSize: int, board: List[str]) -> bool:
        for i in range(boardSize): 
            if "Q" in board[i]: # check for conflicts if there exists a Queen
                if board[i].count("Q") > 1: # Queens in same row
                    return False
                columnToCheck = board[i].index("Q") # Queens in same column
                queens = 0
                for otherRows in range(boardSize): 
                    if board[otherRows][columnToCheck] == "Q":
                        queens += 1
                    if queens > 1: 
                        return False 

                queens = 0 # Diagonals going top left to bottom right
                rowBottomRight, colBottomRight = i + 1, columnToCheck + 1
                rowTopLeft, colTopLeft = i - 1, columnToCheck - 1
                rowBottomLeft, colBottomLeft = i + 1, columnToCheck - 1
                rowTopRight, colTopRight = i - 1, columnToCheck + 1

                while True:
                    canGoBottomRight = (rowBottomRight < boardSize and colBottomRight < boardSize)
                    canGoTopLeft = (rowTopLeft >= 0 and colTopLeft >= 0)
                    canGoBottomLeft = (rowBottomLeft < boardSize and colBottomLeft >= 0)
                    canGoTopRight = (rowTopRight >= 0 and colTopRight < boardSize)

                    if not (canGoBottomRight or canGoTopLeft or canGoBottomLeft or canGoTopRight):
                        break

                    if ((canGoBottomRight and board[rowBottomRight][colBottomRight] == "Q") or 
                        (canGoTopLeft and board[rowTopLeft][colTopLeft] == "Q") or 
                        (canGoBottomLeft and board[rowBottomLeft][colBottomLeft]) == "Q" or
                        (canGoTopRight and board[rowTopRight][colTopRight] == "Q")): 
                        return False # conflicting Queen

                    rowBottomRight += 1
                    colBottomRight += 1

                    rowTopLeft -= 1
                    colTopLeft -= 1

                    rowBottomLeft += 1
                    colBottomLeft -= 1
                
                    rowTopRight -= 1
                    colTopRight += 1
        return True
    
    # Better solution than above: use the slope formula (y+x, y-x) for both diagonals
    # Keep track of queens in the same column with an array `queens`, skip rows when
    # jumping to the next one.
    # xy_dif = diagonal top left to bottom right
    # queens = list of queens placed in spot (column number)
    def solveNQueens(self, board_size):
        def DFS(queens, xy_dif, xy_sum): 
            row = len(queens)
            if row == board_size:
                result.append(queens)
                return None

            # Check for duplicates, conflicts on the diagonal lines, if not, occupy the line
            # and column, adding it to the arrays
            for spot in range(board_size):
                if spot not in queens and row-spot not in xy_dif and row+spot not in xy_sum: 
                    DFS(queens+[spot], xy_dif+[row-spot], xy_sum+[row+spot])  

        # contains a list of numbers showing which columns the queens have been placed
        # starting from the top row
        result = [] 
        DFS([],[],[])
        return [ ["."*i + "Q" + "."*(board_size-i-1) for i in sol] for sol in result]