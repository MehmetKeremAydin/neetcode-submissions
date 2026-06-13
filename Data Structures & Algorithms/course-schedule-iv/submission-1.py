class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def DFS(i, path):
            visited.add(i)
            for elem in path:
                prereqLUT[elem].add(i)
            path.add(i)
            if i in adjMap:
                conns = adjMap[i]
            else:
                return
            for edge in conns:
                if edge in visited:
                    continue
                DFS(edge, path.copy())

        visited = set()
        adjMap = {}
        prereqLUT = {}
        for i in prerequisites:
            conn = adjMap.get(i[1], [])
            conn.append(i[0])
            adjMap[i[1]] = conn
            prereqLUT[i[1]] = set(conn)
        answer = []
        for q in queries:
            if q[1] in prereqLUT and q[0] in prereqLUT[q[1]]:
                answer.append(True)
            else:
                visited.clear()
                DFS(q[1], set())
                if q[1] in prereqLUT and q[0] in prereqLUT[q[1]]:
                    answer.append(True)
                else:
                    answer.append(False)
        return answer
        
        