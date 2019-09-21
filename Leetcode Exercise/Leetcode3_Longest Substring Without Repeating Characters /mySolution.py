class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictCharIndex = dict()
        res = 0
        startIndex = 0
        
        for i in range(len(s)):
            if s[i] in dictCharIndex:
                if  dictCharIndex[s[i]] >= startIndex:
                    res = max(res, (i - dictCharIndex[s[i]]))
                    startIndex = dictCharIndex[s[i]] + 1
                    dictCharIndex[s[i]] = i
                else:
                    dictCharIndex[s[i]] = i
                    res = max(res, i - startIndex + 1)
            else:
                dictCharIndex[s[i]] = i
                res = max(res, i - startIndex + 1)
        return res
                
            