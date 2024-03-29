class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x / div >= 10:
            div = div * 10
            
        while x > 0:
            left = x // div
            right = x % 10
            if left != right:
                return False
            x = (x - left * div) // 10
            div = div // 100
        return True
        