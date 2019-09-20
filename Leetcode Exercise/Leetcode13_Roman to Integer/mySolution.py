class Solution:
    def romanToInt(self, s: str) -> int:
        dictCharNum = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        n = len(s)
        res = 0
        for i in range(n-1, -1, -1):
            if i < (n-1) and dictCharNum[s[i]] < dictCharNum[s[i+1]]:
                res -= dictCharNum[s[i]]
            else:
                res += dictCharNum[s[i]]
        return res