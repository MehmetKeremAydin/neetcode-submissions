class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(i,j, seaMap):
            seaMap[i][j] = True
            for dirc in dircList:
                r, c = i+dirc[0], j+dirc[1]
                if 0<=r<h and 0<=c<w and heights[r][c] >= heights[i][j] and seaMap[r][c] == False:
                    dfs(r,c,seaMap)
            
        dircList = [[0,1],[0,-1], [1,0], [-1,0]]
        h = len(heights)
        w = len(heights[0])
        atlMap = list()
        pacMap = list()
        for i in range(h):
            atlRow = []
            pacRow = []
            for j in range(w):
                if i == 0 or j == 0:
                    pacRow.append(True)
                else:
                    pacRow.append(False)
                if i == h-1 or j == w-1:
                    atlRow.append(True)
                else:
                    atlRow.append(False)
            atlMap.append(atlRow)
            pacMap.append(pacRow)
        for i in range(h):
            for j in range(w):
                if atlMap[i][j] == True:
                    dfs(i,j, atlMap)
                if pacMap[i][j] == True:
                    dfs(i,j, pacMap)
        answer = list()
        for i in range(h):
            for j in range(w):
                if atlMap[i][j] == True and pacMap[i][j] == True:
                    answer.append((i,j))
        return answer
