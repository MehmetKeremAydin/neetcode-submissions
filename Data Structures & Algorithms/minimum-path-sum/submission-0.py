class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def recursiveSearch(m,n):
            if (m,n) in memory: return memory[(m,n)]
            minCost = math.inf
            path1Cost = recursiveSearch(m-1, n) if m-1>=0 else math.inf
            path2Cost = recursiveSearch(m, n-1) if n-1>=0 else math.inf
            minCost = min(path1Cost, path2Cost) + grid[m][n]
            memory[(m,n)] = minCost
            return minCost
        
        memory = {(0,0):grid[0][0]}
        h,w = len(grid), len(grid[0])
        return recursiveSearch(h-1, w-1)