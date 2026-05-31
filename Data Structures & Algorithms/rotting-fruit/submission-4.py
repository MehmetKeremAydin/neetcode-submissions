class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        h = len(grid)
        w = len(grid[0])
        max_steps = 0
        dircList = [[1,0],[-1,0],[0,1],[0,-1]]
        rottens = deque()
        count_fresh = 0
        for i, row in enumerate(grid):
            for j, entry in enumerate(row):
                if entry == 2:
                    rottens.append((i,j, 0))
                if entry == 1:
                    count_fresh += 1
        if count_fresh == 0:
            return 0
        if not rottens:
            return -1
        print(count_fresh)
        while rottens:
            ci, cj, steps = rottens.popleft()
            max_steps = max(max_steps, steps)
            for dirc in dircList:
                r,c = ci + dirc[0], cj + dirc[1]
                if 0<=r<h and 0<=c<w and grid[r][c] == 1:
                    rottens.append((r,c, steps + 1))
                    count_fresh -= 1
                    grid[r][c] = 2
        print(count_fresh)
        if count_fresh == 0:
            return max_steps
        else:
            return -1