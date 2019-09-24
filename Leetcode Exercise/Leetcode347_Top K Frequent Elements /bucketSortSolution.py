class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictNumCounts = dict()
        maxNum = 0
        for num in nums:
            if num in dictNumCounts:
                dictNumCounts[num] += 1
            else:
                dictNumCounts[num] = 1
            if dictNumCounts[num] > maxNum:
                maxNum = dictNumCounts[num]
        bucket = [[] for i in range(maxNum + 1)]
        for num, count in dictNumCounts.items():
            bucket[count].append(num)
        res = []
        for i in range(maxNum, 0, -1):
            if len(res) == k:
                return res
            res +=  bucket[i]
        return res