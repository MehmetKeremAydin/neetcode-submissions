class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjMap = {}
        for i, eq in enumerate(equations):
            edges1 = adjMap.get(eq[0], set())
            edges1.add((eq[1],values[i]))
            adjMap[eq[0]] = edges1
            edges2 = adjMap.get(eq[1], set())
            edges2.add((eq[0],1/values[i]))
            adjMap[eq[1]] = edges2
        #memory = adjMap.copy()
        answer = []
        for q in queries:
            start, target = q[0], q[1]
            queue = deque()
            queue.append((start,1))
            seen = set()
            found = False
            while queue:
                curNode, curRes = queue.popleft()
                if not curNode in adjMap:
                    continue
                for connection in adjMap[curNode]:
                    if connection[0] == target:
                        answer.append(curRes * connection[1])
                        found = True
                        break
                    if not connection[0] in seen:
                        queue.append((connection[0], curRes * connection[1]))
                        seen.add(connection[0])
                if found:
                    break
            if not found:
                answer.append(-1)
        return answer