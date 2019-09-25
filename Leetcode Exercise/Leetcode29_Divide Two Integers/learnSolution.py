class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        postive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            while dividend - tmp >= 0:
                dividend -= tmp
                result += i
                i <<= 1
                tmp <<= 1
        if not postive:
            result = -result
        return min(pow(2, 31) - 1, max(result, pow(-2, 31)-1))