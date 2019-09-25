class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            res = res * 26 + (ord(s[i]) - ord('A') + 1)
        return res