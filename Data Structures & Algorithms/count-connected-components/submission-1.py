class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        notSeen = set([i for i in range(n)])
        adjMap = {i:[] for i in range(n)}
        for edge in edges:
            adjMap[edge[0]].append(edge[1])
            adjMap[edge[1]].append(edge[0])
        numComponents = 0
        while notSeen:
            numComponents += 1
            node = notSeen.pop()
            queue = deque([node])
            while queue:
                node = queue.popleft()
                #print(notSeen, numComponents, queue, adjMap[node])
                for edge in adjMap[node]:
                    if edge in notSeen:
                        notSeen.discard(edge)
                        queue.append(edge)        
        return numComponents
        