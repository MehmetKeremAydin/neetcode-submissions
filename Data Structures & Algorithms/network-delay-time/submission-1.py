class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap = {i:[] for i in range(1,n+1)}
        for edge in times:
            start, end, delay = edge
            adjMap[start].append((end, delay))

        heap = []
        nodesReached = set()
        heapq.heappush(heap, (0, k))
        maxTimeDelay = 0
        while heap and len(nodesReached) < n:
            curDelay, curNode = heapq.heappop(heap)
            if curNode in nodesReached:
                continue
            nodesReached.add(curNode)
            maxTimeDelay = max(maxTimeDelay, curDelay)
            for edge in adjMap[curNode]:
                end, delay = edge
                if not end in nodesReached:
                    heapq.heappush(heap, (curDelay + delay, end))
        return maxTimeDelay if len(nodesReached) == n else -1
