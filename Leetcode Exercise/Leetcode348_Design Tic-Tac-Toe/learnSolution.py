class TicTacToe:

    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.row, self.col = [0]*n, [0]*n
        self.diag1, self.diag2 = 0, 0
        self.n = n

    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            offset = 1
        else:
            offset = -1

        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag1 += offset
        if row + col == self.n - 1:
            self.diag2 += offset

        if self.n in [self.row[row], self.col[col], self.diag1, self.diag2]:
            return 1
        if -self.n in [self.row[row], self.col[col], self.diag1, self.diag2]:
            return 2
        return 0