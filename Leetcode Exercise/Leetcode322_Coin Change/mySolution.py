class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        if amount == 0:
            return 0
        coinChangeArray = [-1] * (amount + 1)
        coins = [i for i in coins if i <= amount]
        for coin in coins:
            coinChangeArray[coin] = 1
        for i in range(1, len(coinChangeArray)):
            for coin in coins:
                if i-coin >= 0 and coinChangeArray[i-coin]>0:
                    if coinChangeArray[i] == -1:
                        coinChangeArray[i] = coinChangeArray[i-coin] + 1
                    else:
                        coinChangeArray[i] = min(coinChangeArray[i], coinChangeArray[i-coin]+1)
        return coinChangeArray[amount]