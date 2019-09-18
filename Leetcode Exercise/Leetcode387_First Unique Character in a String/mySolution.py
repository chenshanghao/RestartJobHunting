class Solution:
    def firstUniqChar(self, s: str) -> int:
        dictCharCount = dict()
        for char in s:
            if char in dictCharCount:
                dictCharCount[char] += 1
            else:
                dictCharCount[char] = 1
        for i in range(len(s)):
            if dictCharCount[s[i]] == 1:
                return i
        return -1