class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        n = len(s)
        for i in range(n):
            res += self.numOfPalindromicSubstringsWithCentre(s, i, i)
        for i in range(1, n):
            res += self.numOfPalindromicSubstringsWithCentre(s, i - 1, i)
        return res
    
    def numOfPalindromicSubstringsWithCentre(self, s, l, r):
        count = 0
        n = len(s)
        if l == r:
            count += 1
            l -= 1
            r += 1
        while l >= 0 and r < n and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        return count