"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def checkLeaf(self, grid, x1, y1, x2, y2):
        check = grid[x1][y1]
        for i in range(x1, x2):
            for j in range(y1, y2):
                if check != grid[i][j]:
                    #print("NOT LEAF@@@: ", x1, y1, x2, y2, i, j)
                    return False, 0
        return True, check

    def construct(self, grid: List[List[int]]) -> 'Node':
        def recursiveBuild(x1, y1, x2, y2):
            #print(x1, y1, x2, y2)
            isLeaf, val = self.checkLeaf(grid, x1, y1, x2, y2)
            if isLeaf:
                #print("LEAF: ", x1, y1, x2, y2)
                qNode = Node(val, isLeaf, None, None, None, None)
            else:
                topLeft = recursiveBuild(x1, y1, (x1+x2)//2, (y1+y2)//2)
                topRight = recursiveBuild(x1, (y1+y2)//2, (x1+x2)//2, y2) 
                bottomLeft = recursiveBuild((x1+x2)//2, y1, x2, (y1+y2)//2)
                bottomRight = recursiveBuild((x1+x2)//2, (y1+y2)//2, x2, y2)
                qNode = Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)
            return qNode
        
        h = len(grid)
        w = len(grid[0])
        return recursiveBuild(0, 0, h, w)