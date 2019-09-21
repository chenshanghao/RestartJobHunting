class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n = len(matrix), len(matrix[0])
        firstRow, firstCol = False, False
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i and j:
                        matrix[i][0] = 0
                        matrix[0][j] = 0
                    else:
                        if i == 0:
                            firstRow = True
                            matrix[0][j] = 0
                        if j == 0:
                            firstCol = True
                            matrix[i][0] = 0                   

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        if firstRow:
            for j in range(n):
                matrix[0][j] = 0
        if firstCol:
            for i in range(m):
                matrix[i][0] = 0
        