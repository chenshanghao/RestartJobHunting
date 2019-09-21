class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        smallIndex, mediumIndex = 0, 0
        for i in range(1, n):
            if nums[i] <= nums[smallIndex]:
                if smallIndex == mediumIndex:
                    smallIndex = i
                    mediumIndex = i
                else:
                    smallIndex = i
            elif nums[i] > nums[smallIndex] and smallIndex == mediumIndex:
                mediumIndex = i
            elif nums[i] > nums[smallIndex] and nums[i] <= nums[mediumIndex]:
                mediumIndex = i
            elif smallIndex != mediumIndex and nums[i] > nums[mediumIndex]:
                return True
        return False
        