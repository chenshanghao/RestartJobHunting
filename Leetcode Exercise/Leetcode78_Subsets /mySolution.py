class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res, nums, [], 0)
        return res
            
    def backtracking(self, res, nums, tmp, start):
        res.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtracking(res, nums, tmp, i + 1)
            tmp.pop()
        
        