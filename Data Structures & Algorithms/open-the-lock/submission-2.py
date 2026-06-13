class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def nextStates(state):
            states = []
            for i in range(4):
                lockInt = int(state[i])
                up = (lockInt + 1)% 10
                down = (lockInt - 1)% 10
                upStr = state[:i] + str(up) + state[(i+1):]
                downStr = state[:i] + str(down) + state[(i+1):]
                states.append(upStr)
                states.append(downStr)
            return states
        
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        queue = deque()
        queue.append(("0000", 0))
        while queue:
            curState, step = queue.popleft()
            if curState == target:
                return step
            for nxt in nextStates(curState):
                if not nxt in deadends:
                    deadends.add(nxt)
                    queue.append((nxt, step+1))
        return -1