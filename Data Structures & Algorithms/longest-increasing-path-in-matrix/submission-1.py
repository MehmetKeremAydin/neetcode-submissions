class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def recursiveSearch(x:int,y:int) -> int:
            if startMem[x][y] != -1: return startMem[x][y]
            dist2End = 1
            for direc in direcList:
                if 0<=x+direc[0]<h and 0<=y+direc[1]<w and matrix[x][y] < matrix[x+direc[0]][y+direc[1]]:
                    curEnd = recursiveSearch(x+direc[0], y+direc[1]) + 1
                    dist2End = max(curEnd, dist2End)
            startMem[x][y] = dist2End
            return dist2End

        h, w = len(matrix), len(matrix[0])
        startMem = [[-1]*w for i in range(h)]
        direcList = [[1,0], [-1,0], [0,1], [0,-1]]
        longestPathLen = 0
        for i in range(h):
            for j in range(w):
                pathLen = recursiveSearch(i,j)
                longestPathLen = max(longestPathLen, pathLen)
        return longestPathLen

        