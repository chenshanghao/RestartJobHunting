class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res
        dictnumVals = {'2': 'abc',
                       '3': 'def',
                       '4': 'ghi',
                       '5': 'jkl',
                       '6': 'mno',
                       '7': 'pqrs',
                       '8': 'tuv',
                       '9': 'wxyz'}
        self.backtracking(res, digits, 0, dictnumVals, '')
        return res
    
    def backtracking(self, res, digits, start, dictnumVals, tmp):
        if len(tmp) == len(digits):
            res.append(tmp[:])
            return
        for i in range(start, len(digits)):
            vals = dictnumVals[digits[i]]
            for char in vals:
                newTmp = tmp + char
                self.backtracking(res, digits, i+1, dictnumVals, newTmp)
            
            