class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        def recJump(i):
            if i in memory:
                return memory[i]
            dist2end = (len(s) - 1) - i 
            if dist2end <= maxJump and dist2end >= minJump:
                memory[i] = True
                return True
            if i > len(s) - 1:
                memory[i] = False
                return False 
            for j in range(maxJump, minJump-1, -1):
                if i+j < len(s) and s[i+j] == "0":
                    result = recJump(i+j)
                    if result:
                        memory[i] = True
                        return True
            memory[i] = False
            return False
        if s[-1] == "1":
            return False
        memory = {}
        return recJump(0)
        