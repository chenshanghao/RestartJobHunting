class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        smallIndex, mediumIndex = 0, -1
        for i in range(1, n):
            if nums[i] <= nums[smallIndex]:
                smallIndex = i
            else:
                if mediumIndex == -1 or nums[i] <= nums[mediumIndex]:
                    mediumIndex = i
                else :
                    return True
        return False
                