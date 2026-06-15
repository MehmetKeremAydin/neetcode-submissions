class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        curLoc = (0,0)
        heap = []
        heapq.heappush(heap, (grid[0][0], curLoc))
        direcList = [[1,0], [-1, 0], [0,1], [0,-1]]
        maxCost = 0
        visited = set()
        while heap:
            cost, curLoc = heapq.heappop(heap)
            if curLoc in visited:
                continue
            visited.add(curLoc)
            maxCost = max(cost, maxCost)
            if curLoc == (h-1,w-1):
                return max(maxCost, cost)
            for direc in direcList:
                px, py = curLoc[0] + direc[0], curLoc[1] + direc[1]
                if 0<=px<h and 0<=py<w and not (px,py) in visited:
                    heapq.heappush(heap, (max(cost, grid[px][py]), (px, py)))
        return maxCost