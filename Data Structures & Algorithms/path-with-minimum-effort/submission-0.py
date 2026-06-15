class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h, w = len(heights), len(heights[0])
        direcList = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = set()
        heap = []
        heapq.heappush(heap, (0,0,0))
        effort = 0
        while heap:
            curEff, x, y = heapq.heappop(heap)
            if x == h-1 and y == w-1:
                return curEff
            if (x,y) in visited:
                continue
            visited.add((x,y))
            for direc in direcList:
                pX, pY = x + direc[0], y + direc[1]
                if 0<=pX<h and 0<=pY<w and not (pX,pY) in visited:
                    heapq.heappush(heap, (max(curEff, abs(heights[x][y]-heights[pX][pY])), pX, pY))
        return -1