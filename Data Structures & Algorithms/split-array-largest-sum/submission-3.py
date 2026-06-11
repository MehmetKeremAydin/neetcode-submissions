class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def DFS(i, remK):
            if (i, remK) in memory:
                return memory[(i, remK)]
            bestResult = math.inf
            if remK > len(nums) - i:
                return math.inf
            elif remK == 1:
                memory[(i, remK)] = sum(nums[i:])
                return memory[(i, remK)]
            partSum = 0
            for j in range(i, len(nums)):
                partSum += nums[j]
                restMax = DFS(j+1, remK-1)
                curAttempt = max(partSum, restMax)
                bestResult = min(bestResult, curAttempt)
            memory[(i, remK)] = bestResult
            return bestResult
        memory = {}
        return DFS(0, k)
        