class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def recursiveSearch(i, target):
            if (i, target) in memory:
                return memory[(i, target)]
            if target == 0:
                return 1
            if i == len(coins) or target < 0:
                return 0
            count1 = recursiveSearch(i, target - coins[i])
            count2 = recursiveSearch(i+1, target)
            memory[(i, target)] = count1 + count2
            return count1 + count2
        memory = {}
        coins = sorted(coins, reverse=True)
        return recursiveSearch(0, amount)
