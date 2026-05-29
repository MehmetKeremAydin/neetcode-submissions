class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i,j):
            grid[i][j] = '0'
            if j+1<w and grid[i][j+1] == '1':
                dfs(i, j+1)
            if j-1>=0 and grid[i][j-1] == '1':
                dfs(i, j-1)
            if i-1>=0 and grid[i-1][j] == '1':
                dfs(i-1, j)
            if i+1<h and grid[i+1][j] == '1':
                dfs(i+1, j)
        
        assert len(grid) > 0
        h = len(grid)
        w = len(grid[0])
        islandCount = 0
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry == '0':
                    continue
                islandCount += 1
                dfs(i,j)
        return islandCount
                