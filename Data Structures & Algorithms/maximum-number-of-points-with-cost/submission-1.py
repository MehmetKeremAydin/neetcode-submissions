class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def recursiveSearch(row:int, i:int) -> int:
            if (row, i) in memory: return memory[(row, i)]
            if row == h:
                return 0
            maxRow = 0
            for j in range(w):
                downTheLine = recursiveSearch(row+1, j)
                currentResult = downTheLine + points[row][j]
                currentResult -= 0 if row == 0 else abs(i-j)
                maxRow = max(maxRow, currentResult)
            memory[(row, i)] = maxRow
            return maxRow
        
        h,w = len(points), len(points[0])
        memory = {}
        return recursiveSearch(0, -5)
        