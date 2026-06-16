class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        h,w = len(grid), len(grid[0])
        heap = []
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited = set()
        while heap:
            curCost, curX, curY = heapq.heappop(heap)
            if curX == h-1 and curY == w-1:
                return curCost
            if (curX,curY) in visited:
                continue
            visited.add((curX, curY))
            if curX + 1 < h and not (curX+1,curY) in visited:
                heapq.heappush(heap, (curCost+grid[curX+1][curY], curX+1, curY))
            if curY + 1 < w and not (curX,curY+1) in visited:
                heapq.heappush(heap, (curCost+grid[curX][curY+1], curX, curY+1))
        
        return -1
        