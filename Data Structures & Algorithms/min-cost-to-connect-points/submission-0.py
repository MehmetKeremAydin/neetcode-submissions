class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjMap = {}
        points = [tuple(i) for i in points]
        for i in range(len(points)):
            p1 = points[i]
            for j in range(i+1, len(points)):
                p2 = points[j]
                dist = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                cons = adjMap.get(p1, [])
                cons.append((dist, p2))
                adjMap[p1] = cons
                cons = adjMap.get(p2, [])
                cons.append((dist, p1))
                adjMap[p2] = cons
        visited = set()
        heap = [(0, points[0])]
        totalCost = 0
        while len(visited) < len(adjMap):
            cost, point = heapq.heappop(heap)
            if point in visited:
                continue
            totalCost += cost
            visited.add(point)
            for edge in adjMap[point]:
                dist, target = edge
                if target in visited:
                    continue
                heapq.heappush(heap, (dist, target))
        return totalCost


