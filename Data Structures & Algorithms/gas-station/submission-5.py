class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        assert len(gas) == len(cost)
        profit = []
        for i in range(len(gas)):
            profit.append(gas[i] - cost[i])
        if sum(profit) < 0:
            return -1
        cumSum = 0
        flag = 0
        for i in range(len(profit)):
            cumSum += profit[i]
            if cumSum < 0:
                cumSum = 0
                flag = i+1

        return flag