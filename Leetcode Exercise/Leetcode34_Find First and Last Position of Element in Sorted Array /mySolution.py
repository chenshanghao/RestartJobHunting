class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        if nums[0] > target or nums[-1] < target:
            return [-1, -1]
        leftBoundary, rightBoundary = -1, -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                if mid > 0 and nums[mid-1] == target:
                    r = mid - 1
                else:
                    leftBoundary = mid
                    break
        if leftBoundary == -1:
            return [-1, -1]
                    
        l, r = leftBoundary, len(nums) - 1  
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif mid < (len(nums) - 1) and nums[mid + 1] == target:
                l = mid + 1
            else:
                rightBoundary = mid
                break
        return [leftBoundary, rightBoundary]
            
                