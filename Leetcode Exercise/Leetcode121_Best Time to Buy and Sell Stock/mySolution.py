class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        res = 0
        if n <= 1:  return res
        smallVal = prices[0]
        for i in range(1, n):
            if prices[i] < smallVal:
                smallVal = prices[i]
            else:
                res = max(res, prices[i] - smallVal)
        return res