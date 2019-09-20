# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        return self.findFirstBadVersion(1, n)
        
    
    def findFirstBadVersion(self, left, right):
        if right - left <= 1:
            return left if isBadVersion(left) else right
        mid = (left + right) // 2
        if not isBadVersion(mid):
            return self.findFirstBadVersion(mid + 1, right)
        elif isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        else:
            return self.findFirstBadVersion(left, mid - 1)
        
        
        
        
        