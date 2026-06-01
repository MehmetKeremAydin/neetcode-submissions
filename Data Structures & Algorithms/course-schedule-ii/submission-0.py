class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(node, seen):
            if node in seen:
                return True # There is a loop!
            seen.add(node)
            while adjMap[node]:
                edge = adjMap[node].pop()
                if not edge in toBeTaken:
                    continue
                looped = dfs(edge, seen)
                if looped:
                    return True # Loop found.
            seen.remove(node)
            toBeTaken.remove(node)
            answer.append(node)
            return False
            
        answer = []
        adjMap = {i:[] for i in range(numCourses)}
        for preq in prerequisites:
            adjMap[preq[0]].append(preq[1])
        toBeTaken = set([i for i in range(numCourses)])
        while toBeTaken:
            node = toBeTaken.pop()
            toBeTaken.add(node)
            seen = set()
            looped = dfs(node, seen)
            if looped:
                return []
        
        return answer