class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(res, sorted(nums), [], 0)
        return res
        
    def backtracking(self, res, nums, tmp, start):
        res.append(tmp[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            tmp.append(nums[i])
            self.backtracking(res, nums, tmp, i+1)
            tmp.pop()