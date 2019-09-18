class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        index = 0
        if n == 0:
            return index
        for i in range(1, n):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index + 1
        