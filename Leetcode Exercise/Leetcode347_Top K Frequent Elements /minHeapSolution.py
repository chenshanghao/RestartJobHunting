import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictNumCount = dict()
        for num in nums:
            if num in dictNumCount:
                dictNumCount[num] += 1
            else:
                dictNumCount[num] = 1
        minHeap = [(-count, num) for num, count in dictNumCount.items()]
        heapq.heapify(minHeap)
        return [ heapq.heappop(minHeap)[1] for i in range(k)]