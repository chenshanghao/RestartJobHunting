class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board or not board[0]:
            return False
        m, n = len(board), len(board[0])
        visited = [[False for i in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j] and self.dfs(m, n, i, j, word, board, visited):
                    return True
        return False
    
    def dfs(self, m, n, i, j, word, board, visited):
        if word == '':
            return True
        if i < 0 or i == m or j < 0 or j == n or visited[i][j] or board[i][j] != word[0]:
            return False
        visited[i][j] = True
        newWord = word[1:]
        res = self.dfs(m, n, i-1, j, newWord, board, visited) or self.dfs(m, n, i, j-1, newWord, board, visited) or self.dfs(m, n, i+1, j, newWord, board, visited) or self.dfs(m, n, i, j+1, newWord, board, visited)
        if res:
            return True
        visited[i][j] = False
                    