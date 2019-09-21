class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = 0 - nums[i]
            l, r = i+1, n-1
            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                if r < n-1 and nums[r] == nums[r+1]:
                    r -= 1
                    continue
                if nums[l] + nums[r] == target:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return res
            
        
        