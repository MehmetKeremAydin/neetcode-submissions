class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(queue):
            #print('NEW')
            curLen = 0
            while queue:
                #print(queue)
                curLen += 1
                entry = queue.popleft()
                row, col = entry
                grid[row][col] = 0
                dircList = [[-1, 0], [1,0], [0,1], [0,-1]]
                for dirc in dircList:
                    r, c = row + dirc[0], col + dirc[1]
                    if 0<=r<h and 0<=c<w and grid[r][c] == 1:
                        queue.append((r, c))
                        grid[r][c] = 0
            return curLen

            
            
        
        assert len(grid) > 0
        h = len(grid)
        w = len(grid[0])
        maxSize = 0
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry == 1:
                    searchQueue = deque()
                    searchQueue.append((i,j))
                    size = bfs(searchQueue)
                    maxSize = max(size, maxSize)
        return maxSize