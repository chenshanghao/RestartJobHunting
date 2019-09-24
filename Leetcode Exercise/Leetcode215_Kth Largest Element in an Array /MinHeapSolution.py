import heapq

# https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/301338/Python-or-tm-215

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [-float('inf')] * k
        heapq.heapify(minHeap)
        for num in nums:
            if num > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, num)
        return minHeap[0]
        