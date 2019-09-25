class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        sumOfSquareList = []
        sumOfSquare = 0
        while True:
            sumOfSquare = 0
            while n > 0:
                tail = n % 10
                n = n // 10
                sumOfSquare += tail * tail
            if sumOfSquare == 1:
                return True
            if sumOfSquare in sumOfSquareList:
                return False
            sumOfSquareList.append(sumOfSquare)
            n = sumOfSquare

        