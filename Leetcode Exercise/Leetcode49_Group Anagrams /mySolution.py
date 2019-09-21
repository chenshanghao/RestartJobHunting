class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictWordIndex = dict()
        lastIndex = 0
        res = []
        for word in strs:
            tmp = str(sorted(word))
            if tmp in dictWordIndex:
                res[dictWordIndex[tmp]].append(word)
            else:
                dictWordIndex[tmp] = lastIndex
                res.append([word])
                lastIndex += 1
        return res
                
            
        