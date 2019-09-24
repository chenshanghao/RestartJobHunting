class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = 0, 0, 0
        for index in range(len(nums)):
            if nums[index] == 0:
                nums[k] = 2
                nums[j] = 1
                nums[i] = 0
                i += 1
                j += 1
                k += 1
            elif nums[index] == 1:
                nums[k] = 2
                nums[j] = 1
                j += 1
                k += 1
            else:
                nums[k] = 2
                k += 1
                
                
        