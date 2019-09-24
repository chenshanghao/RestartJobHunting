# Max Heap
# Time: O(n + klog(n)) | Space: O(n)
# Time Complexity：Heapify用了O(N)，
# 然后一共pop了k个元素，每个元素使用logn的时间复杂，所以一共是O(n + klog(n))



import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res