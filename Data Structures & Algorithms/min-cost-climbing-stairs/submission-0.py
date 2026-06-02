class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        def recursiveCost(n):
            if n in alreadySeen:
                return alreadySeen[n]
            if n == lenStairs + 1:
                return 9999999
            if n == lenStairs:
                return 0
            cost_a = recursiveCost(n+1) + cost[n]
            cost_b = recursiveCost(n+2) + cost[n]
            alreadySeen[n] = min(cost_a, cost_b)
            return alreadySeen[n]
            
        lenStairs = len(cost)
        alreadySeen = {}
        return min(recursiveCost(0), recursiveCost(1))