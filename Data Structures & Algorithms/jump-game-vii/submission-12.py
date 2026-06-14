class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        queue = deque()
        queue.append(0)
        maxReach = 0
        if s[-1] == "1":
            return False 
        while queue:
            curIsland = queue.popleft()
            if curIsland == len(s) - 1:
                return True
            for i in range(minJump, maxJump+1):
                if curIsland + i > maxReach and curIsland + i < len(s) and s[curIsland + i] == "0":
                    maxReach = curIsland + i
                    queue.append(curIsland + i)
        return False
                