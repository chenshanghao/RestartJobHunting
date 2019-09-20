class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res = nums[0]
        indexSum = 0 if nums[0] < 0 else nums[0]
        for i in range(1, len(nums)):
            res = max(res, indexSum + nums[i])
            if indexSum + nums[i] < 0:
                indexSum = 0
            else:
                indexSum += nums[i]
        return res
            