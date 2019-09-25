# numerator      分子
# denominator    分母
# quotient       商
# remainder      余数
# divmod return quotient, denominator

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = ''
        if not ((numerator < 0) is (denominator < 0)):
            res += '-'
        if numerator % denominator == 0:
            return str(numerator//denominator)
        numerator, denominator = abs(numerator), abs(denominator)
        res += str(numerator//denominator) + '.'
        numerator = numerator % denominator
        i = len(res)
        table = dict()
        while numerator != 0:
            if numerator not in table:
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + '(' + res[i:] + ')'
                return res
            numerator = numerator * 10
            res += str(numerator//denominator)
            numerator%=denominator
            i+=1
        return res
        