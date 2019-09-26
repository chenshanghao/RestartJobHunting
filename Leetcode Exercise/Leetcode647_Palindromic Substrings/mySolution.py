class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        for i in range(n):
            res += self.numOfPalindromicSubstingWithCentre(s, i, i)
        for i in range(1, n):
            res += self.numOfPalindromicSubstingWithCentre(s, i - 1, i)
        return res
    
    def numOfPalindromicSubstingWithCentre(self, s, l, r):
        count = 0
        if l == r:
            count += 1
            l -= 1
            r += 1
        n = len(s) - 1
        while l >= 0 and r <= n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count
            
        
        
        