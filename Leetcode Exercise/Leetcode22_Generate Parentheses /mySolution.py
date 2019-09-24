class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n == 0:
            return res
        self.backtracking(res, 0, 0, n, '')
        return res
        
    def backtracking(self, res, left, right, n, tmp):
        if right > left or left > n:
            return
        if right == left and right == n:
            res.append(tmp[:])
        self.backtracking(res, left + 1, right, n, tmp[:] + '(')
        self.backtracking(res, left, right + 1, n, tmp[:] + ')')