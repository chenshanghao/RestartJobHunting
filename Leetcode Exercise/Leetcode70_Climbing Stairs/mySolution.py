class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        res = [1, 1]
        for i in range(2, n):
            res = [res[1], sum(res)]
        return sum(res)