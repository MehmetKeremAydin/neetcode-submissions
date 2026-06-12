class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # We first find a starting position. 
        h = len(grid)
        w = len(grid[0])
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
        print(start)
        direcL = [(1,0), (-1,0), (0,1), (0,-1)]
        stack = [start]
        seen = set()
        seen.add(start)
        perimeter = 0
        while stack:
            curCord = stack.pop()
            for direc in direcL:
                proposed = (curCord[0] + direc[0], curCord[1] + direc[1])
                if 0<=proposed[0]<h and 0<=proposed[1]<w:
                    if grid[proposed[0]][proposed[1]] == 0:
                        perimeter += 1
                    elif not proposed in seen:
                        seen.add(proposed)
                        stack.append(proposed)
                else:
                    perimeter += 1
            print(curCord, perimeter)
        return perimeter
