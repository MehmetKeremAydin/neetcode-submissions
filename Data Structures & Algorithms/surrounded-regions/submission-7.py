class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(i:int,j:int, curSeen:set)->bool:
            if i==0 or i==h-1 or j==0 or j==w-1:
                flag = True
            else:
                flag = False
            for dirc in dircList:
                r,c = i+dirc[0], j+dirc[1]
                if 0<=r<h and 0<=c<w and board[r][c] == 'O' and not (r,c) in curSeen:
                    curSeen.add((r,c))
                    otherFlag = dfs(r,c, curSeen)
                    flag = otherFlag or flag
            return flag
        
        dircList = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        h = len(board)
        w = len(board[0])
        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                if board[i][j] == 'X' or (i,j) in visited:
                    continue
                current = set()
                current.add((i,j))
                touchingSide = dfs(i,j,current)
                if not touchingSide:
                    for entry in current:
                        board[entry[0]][entry[1]] = "X"
                visited = visited.union(current)
                
        