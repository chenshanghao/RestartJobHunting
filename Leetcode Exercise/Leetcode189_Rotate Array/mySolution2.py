class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        self.reverseArray(nums, 0, n - 1)
        self.reverseArray(nums, 0, k - 1)
        self.reverseArray(nums, k, n - 1)
    
    def reverseArray(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1