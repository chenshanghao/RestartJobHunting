class Solution:
    def myAtoi(self, str: str) -> int:
        res = 0
        sign = 1
        n = len(str)
        i = 0
        while(i < n):
            if str[i] == '+':
                i += 1
                break
            elif str[i] == '-':
                i += 1
                sign = -1
                break
            elif str[i].isdigit():
                break
            elif str[i] == ' ':
                i += 1
            else:
                return 0
        while(i<n and str[i].isdigit()):
            res = res * 10 + int(str[i])
            i += 1
        res = res * sign
        if res < pow(-2, 31):
            return pow(-2, 31)
        if res > pow(2,31) -1:
            return pow(2,31) -1
        return res
            