class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        connMap = {}
        for edge in edges:
            if edge[0] in connMap:
                connMap[edge[0]].append(edge[1])
            else:
                connMap[edge[0]] = [edge[1]]
            if edge[1] in connMap:
                connMap[edge[1]].append(edge[0])
            else:
                connMap[edge[1]] = [edge[0]]
        if not edges:
            return False if n > 1 else True
        seen = set()
        queue = deque()
        print(edges)
        queue.append((-1, edges[0][0]))
        seen.add(edges[0][0])
        while queue:
            cameFrom, node = queue.popleft()
            for edge in connMap[node]:
                if edge in seen and edge != cameFrom:
                    return False
                if edge != cameFrom:
                    queue.append((node, edge))
                    seen.add(edge)
        return True if len(seen) == n else False





        