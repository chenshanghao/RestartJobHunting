class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isRowValid(board) and self.isColValid(board) and self.isSquareValid(board)
    
    def isRowValid(self, board):
        for row in range(9):
            if not self.isUnitValid(board[row]):
                return False
        return True
    
    def isColValid(self, board):
        for i in range(9):
            unit = []
            for j in range(9):
                unit.append(board[j][i])
            if not self.isUnitValid(unit):
                return False
        return True
    
    def isSquareValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                square = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isUnitValid(square):
                    return False
        return True
    
    def isUnitValid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(set(unit)) == len(unit)