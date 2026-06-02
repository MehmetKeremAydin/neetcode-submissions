class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remaining:int, coinCount:int):
            if (remaining, coinCount) in hashMap:
                return hashMap[(remaining, coinCount)]
            if remaining == 0:
                #print(remaining, coinCount)
                return True, coinCount
            elif remaining < 0:
                return False, 0
            bestCount = 100001
            foundOnce = False
            for coin in coins:
                found = False
                found, count = dfs(remaining - coin, coinCount+1)
                if found:
                    foundOnce = True
                    bestCount = min(bestCount, count)
            hashMap[(remaining, coinCount)] = (True, bestCount) if foundOnce else (False, -1)
            return hashMap[(remaining, coinCount)]
        hashMap = {}
        coins = sorted(coins)
        found, count = dfs(amount, 0)
        return count if found else -1
        
            
        