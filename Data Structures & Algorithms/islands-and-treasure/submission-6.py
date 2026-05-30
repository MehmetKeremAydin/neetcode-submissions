class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def dfs(step, i, j):
            grid[i][j] = min(grid[i][j], step)
            for direc in dirList:
                r, c = i + direc[0], j + direc[1]
                if (not 0<=r<h) or (not 0<=c<w) or (grid[r][c] < step):
                    continue
                dfs(step+1, r, c) 
            return

        dirList = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0:
                    dfs(0, i, j)
        return
        