class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def findGroup(node):
            for i, nodeGrp in enumerate(nodeGrpLUT):
                if node in nodeGrp:
                    return i
            else:
                return -1
        
        nodeGrpLUT = [set([i]) for i in range(1, len(edges)+1)]
        for edge in edges:
            #print(nodeGrpLUT)
            curNode = edge[0]
            testNode = edge[1]
            curGroup = findGroup(curNode)
            testGroup = findGroup(testNode)
            if curGroup == testGroup:
                return edge
            nodeGrpLUT[curGroup] = nodeGrpLUT[curGroup].union(nodeGrpLUT[testGroup])
            nodeGrpLUT.pop(testGroup)
        return []