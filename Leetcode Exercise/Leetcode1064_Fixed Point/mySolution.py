class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return False

        left, right = 0, len(A) - 1
        while left <= right:
            mid = (left + right) // 2
            if A[mid] == mid:
                return mid
            elif mid < A[mid]:
                right =  mid - 1
            else:
                left = mid + 1
        return -1