class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        if not strs:
            return res
        for i in range(len(strs[0])):
            tmp = strs[0][i]
            for string in strs:
                if i == len(string):
                    return res
                if string[i] != tmp:
                    return res
            res += tmp
        return res
            