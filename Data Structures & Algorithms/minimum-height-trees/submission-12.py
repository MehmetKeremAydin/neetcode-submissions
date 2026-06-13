class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        ranks = [0] * n
        adjMap = {}
        for edge in edges:
            ranks[edge[0]] += 1
            ranks[edge[1]] += 1
            conn = adjMap.get(edge[0], set())
            conn.add(edge[1])
            adjMap[edge[0]] = conn
            conn = adjMap.get(edge[1], set())
            conn.add(edge[0])
            adjMap[edge[1]] = conn
        availableNodes = set([i for i in range(n)])
        while len(availableNodes) > 2:
            toBeRemoved = []
            for i,entry in enumerate(ranks):
                if i in availableNodes and entry <= 1:
                    toBeRemoved.append(i)
                    availableNodes.discard(i)
            for leaf in toBeRemoved:
                leafCons = adjMap[leaf]
                for parents in leafCons:
                    ranks[parents] -= 1
        return list(availableNodes)
        
        