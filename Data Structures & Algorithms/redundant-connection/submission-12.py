class UnionFind():
    def __init__(self, n:int):
        self.parents = [i for i in range(n)]
        self.rank = [1 for _ in range(n)]
        self.numNodes = n

    def find(self, i:int):
        if i != self.parents[i]:
            self.parents[i] = self.find(self.parents[i])
        return self.parents[i]


    def union(self, i:int, j:int):
        pi, pj = self.find(i), self.find(j)
        if pi == pj:
            return False
        if self.rank[pi] > self.rank[pj]:
            self.parents[pj] = pi
            self.rank[pi] += self.rank[pj]
        else:
            self.parents[pi] = pj
            self.rank[pj] += self.rank[pi]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        nodes = set()
        for e in edges:
            nodes.add(e[0])
            nodes.add(e[1])
        dsu = UnionFind(len(nodes))
        for e in edges:
            node1, node2 = e
            if not dsu.union(node1-1, node2-1):
                return e
        return -1
        