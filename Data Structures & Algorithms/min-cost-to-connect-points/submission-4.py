class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def getDist(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        adjMap = {i:set([]) for i in range(len(points))}
        for i in range(len(points)):
            for j in range(1, len(points)):
                dist = getDist(points[i], points[j])
                adjMap[i].add((dist, j))
                adjMap[j].add((dist, i))
        totalCost = 0
        heap = [(0, 0)]
        alreadyConnected = set()
        while heap and len(alreadyConnected) < len(points):
            cost, node = heapq.heappop(heap)
            if node in alreadyConnected:
                continue
            alreadyConnected.add(node)
            totalCost += cost
            for edge in adjMap[node]:
                if edge[1] in alreadyConnected: continue
                heapq.heappush(heap, (edge[0], edge[1]))
        return totalCost
        
