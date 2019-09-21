class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        res = ''
        if n == 0:
            return res
        if n == 1:
            return s
        
        res = s[0]
        dp = [[False for i in range(n)] for j in range(n)]
        for i in range(n):
            dp[i][i] = True
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res = s[i: i+2]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if dp[i+1][j-1] and s[i] == s[j]:
                    if len(s[i: j+1]) > len(res):
                        res = s[i: j+1]
                    dp[i][j] = True
        return res
                    