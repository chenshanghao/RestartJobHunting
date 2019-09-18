class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictNumCount = dict()
        for num in nums:
            if num in dictNumCount:
                return True
            else:
                dictNumCount[num] = 1
        return False