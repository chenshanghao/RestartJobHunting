class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        res = [[1]]
        for i in range(1, numRows):
            tmp = res[-1]
            newRow = [tmp[0]] + [tmp[i] + tmp[i+1] for i in range(len(tmp) - 1)] + [tmp[-1]]
            res.append(newRow)
        return res
            