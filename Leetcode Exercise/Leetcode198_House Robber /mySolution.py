class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n <= 2:
            return max(nums)
        res = [nums[0], nums[1]]
        for i in range(2, n):
            res = [max(res[0], res[1]), res[0] + nums[i]]
        return max(res)
        