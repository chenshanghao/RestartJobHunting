class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            tmp =self.findLongestPalindromicSubstrWithFixedCentral(s, i, i)
            res = tmp if len(res) < len(tmp) else res
            if i > 0:
                tmp = self.findLongestPalindromicSubstrWithFixedCentral(s, i-1, i)
                res = tmp if len(res) < len(tmp) else res
        return res
    
    def findLongestPalindromicSubstrWithFixedCentral(self, s, l, r):
        leftBoundary, rightBoundary = 0, len(s) - 1
        while l >= leftBoundary and r <= rightBoundary and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1: r]
        
        
        