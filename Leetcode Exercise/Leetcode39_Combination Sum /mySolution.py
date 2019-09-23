class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.batcktracking(sorted(candidates), target, [], 0, res)
        return res
        
    def batcktracking(self, candidates, target, tmp, start, res):
        if sum(tmp) == target:
            res.append(tmp[:])
            return
        if sum(tmp) > target:
            return
        
        for i in range(start, len(candidates)):
            tmp.append(candidates[i])
            self.batcktracking(candidates, target, tmp, i, res)
            tmp.pop()
        