import math

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        tmp = [0] * (n)
        upper = int(math.sqrt(n))
        for i in range(2, upper + 1):
            if tmp[i] == 1:
                continue
            pointer = i + i
            while(pointer < n):
                tmp[pointer] = 1
                pointer += i
        res = 0
        for i in range(2, n):
            if tmp[i] == 0:
                res += 1
        return res
                