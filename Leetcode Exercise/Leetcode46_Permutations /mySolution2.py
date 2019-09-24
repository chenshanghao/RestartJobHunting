class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        self.backtracking(res, nums, [])
        return res
        
        
    def backtracking(self, res, nums, tmp):
        if len(tmp) == len(nums):
            res.append(tmp[:])
            return
        for num in nums:
            if num in tmp:
                continue
            tmp.append(num)
            self.backtracking(res, nums, tmp)
            tmp.pop()