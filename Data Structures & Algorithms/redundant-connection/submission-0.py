class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def dfs(node):
            if node in cycle: #improve?
                idx = cycle.index(node)
                cycle.append(node)
                return (True, idx) # loop found
            cycle.append(node)
            for edge in adjMap[node]:
                if len(cycle) >= 2 and edge[0] == cycle[-2]:
                    continue
                cycleFound, idx = dfs(edge[0])
                if cycleFound:
                    return True, idx
            cycle.pop()
            return False, -1

        listIdx = {}    
        adjMap = {}
        for i, edge in enumerate(edges):
            listIdx[tuple(edge)] = i
            if edge[0] in adjMap:
                adjMap[edge[0]].add((edge[1],i))
            else:
                adjMap[edge[0]] = set()
                adjMap[edge[0]].add((edge[1], i))
            if edge[1] in adjMap:
                adjMap[edge[1]].add((edge[0],i))
            else:
                adjMap[edge[1]] = set()
                adjMap[edge[1]].add((edge[0], i))
        toBeVisited = set([key for key in adjMap])
        node = edges[0][0]
        cycle = []
        loopFound, idx = dfs(node)
        loop = cycle[idx:]
        latest_idx = 0
        answer = [0,0]
        for i in range(1, len(loop)):
            frm = min(loop[i-1], loop[i])
            to = max(loop[i-1], loop[i])
            curListIdx = listIdx[(frm, to)]
            if curListIdx > latest_idx:
                latest_idx = curListIdx
                answer = [frm, to]
        return answer