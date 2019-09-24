class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, res, [], 0)
        return res
        
    def backtracking(self, nums, res, tmp, start):
        res.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtracking(nums, res, tmp, i+1)
            tmp.pop()
        