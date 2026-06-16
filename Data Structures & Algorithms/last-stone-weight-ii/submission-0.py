class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        def recursiveSearch(i, target):
            if (i, target) in memory:
                return memory[(i, target)]
            if target <= 0 or i == len(stones):
                return target
            result1 = recursiveSearch(i+1, target-stones[i])
            result2 = recursiveSearch(i+1, target)
            if abs(result1) < abs(result2): 
                memory[(i, target)] = result1
                return result1
            else: 
                memory[(i, target)] = result2
                return result2
        

        memory = {}
        total = sum(stones)
        target = total // 2
        closestRes2Target = recursiveSearch(0, target)
        g1 = target - closestRes2Target
        g2 = total - g1
        return abs(g1 - g2)
        