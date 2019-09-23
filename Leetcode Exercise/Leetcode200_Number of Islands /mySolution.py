class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if not grid or not grid[0]:
            return res
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    self.fillIslands(grid, i, j, m, n)
        return res
    
    def fillIslands(self, grid, i, j, m, n):
        if not (i >= 0 and i < m and j >= 0 and j < n):
            return
        if grid[i][j] == '0':
            return
        grid[i][j] = '0'
        self.fillIslands(grid, i-1, j, m, n)
        self.fillIslands(grid, i, j-1, m, n)
        self.fillIslands(grid, i+1, j, m, n)
        self.fillIslands(grid, i, j+1, m, n)
        
            