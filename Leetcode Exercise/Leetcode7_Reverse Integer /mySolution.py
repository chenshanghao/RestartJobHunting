class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        res = 0
        while(x):
            carry = x % 10
            x = x // 10
            res = res * 10 + carry
        res = res * sign
        if  pow(-2,31) <= res <= (pow(2,31) -1):
            return res
        else:
            return 0