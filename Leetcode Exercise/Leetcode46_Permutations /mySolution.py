class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, res, [])
        return res
    
    def backtracking(self, nums, res, tmp):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for num in nums:
            if num not in tmp:
                tmp.append(num)
                self.backtracking(nums, res, tmp)
                tmp.pop()