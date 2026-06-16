class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        edgeLUT = {i:edge for i,edge in enumerate(edges)}
        for i, edge in enumerate(edges): edge.append(i)
        edgesSorted = sorted(edges, key=lambda x:x[2])
        edgesSorted = [edge[3] for edge in edgesSorted]
        baseParent = [i for i in range(n)]
        baseRank = [1] * n
        #print(edgesSorted)
        #print(edgeLUT)
        def find(i, parent):
            while  i != parent[i]:
                i = parent[i]
            return i
        def union(i,j, parent, rank):
            pi,pj = find(i, parent), find(j, parent)
            if pi == pj: return False
            if rank[pi] >= rank[pj]:
                rank[pi] += rank[pj]
                parent[pj] = pi
            else:
                rank[pj] += rank[pi]
                parent[pi] = pj
            return True
        MST = []
        candidates = []
        baseCost = 0
        for edgeIdx in edgesSorted:
            src, dst, weight, _ = edgeLUT[edgeIdx]
            result = union(src, dst, baseParent, baseRank)
            if result:
                MST.append(edgeIdx)
                baseCost += weight
            else:
                candidates.append(edgeIdx)
            if max(baseRank) == n:
                break
        start = edgesSorted.index(edgeIdx) + 1
        while start < len(edgesSorted) and edgeLUT[edgesSorted[start]][2] == weight:
            candidates.append(edgesSorted[start])
            start += 1
        #print(MST)
        #print(candidates)
        if not candidates:
            return [MST, []]
        critical = set()
        pseudo = set()
        for i in range(len(MST)):
            temp = MST.copy()
            removed = temp.pop(i)
            testParent = [i for i in range(n)]
            testRank = [1] * n
            testCost = 0
            for edgeIdx in temp:
                src, dst, weight, _ = edgeLUT[edgeIdx]
                result = union(src, dst, testParent, testRank)
                testCost += weight
            isPseudo = False
            for candIdx in candidates:
                candidateParent, candidateRank = testParent.copy(), testRank.copy()
                src, dst, weight, _ = edgeLUT[candIdx]
                result = union(src, dst, candidateParent, candidateRank)
                if result and testCost + weight == baseCost:
                    pseudo.add(removed)
                    pseudo.add(candIdx)
                    isPseudo = True
            if not isPseudo:
                critical.add(removed)

        return [list(critical), list(pseudo)]