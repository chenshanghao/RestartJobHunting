class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.powCalc(x, -n)
        else:
            return self.powCalc(x, n)
    
    
    def powCalc(self, a, b):
        if b == 0:
            return 1
        half = self.powCalc(a, b//2)
        if b % 2 == 0:
            return half * half
        else:
            return half * half * a
        