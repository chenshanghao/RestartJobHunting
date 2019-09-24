class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <=1:
            return n
        results = []
        for index, num in enumerate(nums):
            result = 1
            for i in range(index):
                if nums[i] < num:
                    result = max(result, results[i]+1)
            results.append(result)
        return max(results)