class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        cap2prof = sorted(zip(capital, profits))
        doableTasks = []
        j = 0
        for i in range(k):
            while j < len(cap2prof) and cap2prof[j][0] <= w:
                heapq.heappush_max(doableTasks, cap2prof[j][1])
                j += 1
            if doableTasks:
                w += heapq.heappop_max(doableTasks)
            else:
                return w
        return w