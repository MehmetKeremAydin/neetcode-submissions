class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        costToGet = [0] * (len(cost) + 1)
        for i in range(2, len(cost)+1):
            costToGet[i] = min(costToGet[i-1]+cost[i-1], costToGet[i-2]+cost[i-2])
        return costToGet[-1]
