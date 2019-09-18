class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictCharNum = dict()
        for char in s:
            if char not in dictCharNum:
                dictCharNum[char] = 1
            else:
                dictCharNum[char] += 1
        
        for char in t:
            if char in dictCharNum and dictCharNum[char] > 0:
                dictCharNum[char] -= 1
            else:
                return False
        return True