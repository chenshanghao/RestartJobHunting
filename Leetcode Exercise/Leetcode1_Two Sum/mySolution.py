class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictNumIndex = {}
        for i in range(len(nums)):
            if target - nums[i] in dictNumIndex:
                return [dictNumIndex[target - nums[i]], i]
            else:
                dictNumIndex[nums[i]] = i