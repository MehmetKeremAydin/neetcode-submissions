class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recursiveCost(n):
            if n in alreadySeen:
                return alreadySeen[n]
            if n == lenStairs + 1:
                return -1
            if n == lenStairs:
                return 0
            cost_a = recursiveCost(n+1)
            cost_b = recursiveCost(n+2)
            if cost_b == -1:
                cost_b = cost_a
            alreadySeen[n] = min(cost_a, cost_b) + cost[n]
            return alreadySeen[n]
            
        lenStairs = len(cost)
        alreadySeen = {}
        return min(recursiveCost(0), recursiveCost(1))