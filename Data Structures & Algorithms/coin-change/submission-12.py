class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coinCount = [math.inf] * (amount + 1)
        coinCount[0] = 0
        coins = sorted(coins)
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    coinCount[i] = min(coinCount[i], coinCount[i-coin] + 1)
        return coinCount[-1] if coinCount[-1] != math.inf else -1