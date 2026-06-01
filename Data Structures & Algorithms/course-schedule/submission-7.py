class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node, seen):
            if node in seen:
                return True
            seen.add(node)
            while adjMap[node]:
                newNode = adjMap[node].pop()
                if not newNode in toBeTaken: # class is already taken
                    continue
                looped = dfs(newNode, seen)
                if looped:
                    return True
            toBeTaken.discard(node)
            seen.discard(node)
            return False


        adjMap = {i:set([]) for i in range(numCourses)}
        for preq in prerequisites:
            adjMap[preq[0]].add(preq[1])
        toBeTaken = set([i for i in range(numCourses)])
        while toBeTaken:
            node = toBeTaken.pop()
            toBeTaken.add(node)
            seen = set()
            looped = dfs(node, seen)
            if looped:
                return False

        return True
        