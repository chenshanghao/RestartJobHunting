class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        lastIndex = len(nums) - 1
        maximumIndex = 0
        for i in range(lastIndex + 1):
            if maximumIndex < i:
                break
            maximumIndex = max(maximumIndex, i + nums[i])
            if maximumIndex >= lastIndex:
                return True
        return False
            
        