class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        def recursiveBurst(baloons:list) -> int:
            if tuple(baloons) in memory: return memory[tuple(baloons)]
            if len(baloons) == 2:
                return 0
            maxCoins = 0
            for i in range(1, len(baloons)-1):
                curCoins = baloons[i-1] * baloons[i] * baloons[i+1]
                newBaloons = list(baloons)
                newBaloons.pop(i)
                profit = recursiveBurst(newBaloons) + curCoins
                maxCoins = max(maxCoins, profit)
            memory[tuple(baloons)] = maxCoins
            return maxCoins
        memory = {}
        nums.insert(0, 1)
        nums.append(1)
        return recursiveBurst(nums)