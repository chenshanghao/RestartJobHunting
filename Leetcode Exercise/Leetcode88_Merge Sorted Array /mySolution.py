class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums1:
            return 
        tail = len(nums1) - 1
        m, n = m - 1, n - 1
        while n >= 0 and m >= 0:
            if nums1[m] < nums2[n]:
                nums1[tail] = nums2[n]
                n -= 1
            else:
                nums1[tail] = nums1[m]
                m -= 1
            tail -= 1
        while n >= 0:
            nums1[tail] = nums2[n]
            n -= 1
            tail -= 1
            
        