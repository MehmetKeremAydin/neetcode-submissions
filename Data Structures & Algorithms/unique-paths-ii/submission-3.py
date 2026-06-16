class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def recursiveSearch(m,n):
            if (m,n) in memory: return memory[(m,n)]
            if m < 0 or n < 0 or obstacleGrid[m][n] == 1: return 0
            numPaths = 0
            numPaths += recursiveSearch(m-1, n) if m-1>=0 else 0
            numPaths += recursiveSearch(m, n-1) if n-1>=0 else 0
            memory[(m,n)] = numPaths
            return numPaths
      
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1]:
            return 0
        memory = {(0,0):1}
        h,w = len(obstacleGrid), len(obstacleGrid[0])
        return recursiveSearch(h-1,w-1)
        