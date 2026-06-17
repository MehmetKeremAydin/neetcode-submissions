class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursiveMatch(i:int, j:int) -> bool:
            if (i,j) in memory: return memory[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                memory[(i,j)] = False
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                memory[(i,j)] = recursiveMatch(i,j+2) or (match and recursiveMatch(i+1, j))
                return memory[(i,j)]
            if match:
                memory[(i,j)] = recursiveMatch(i+1, j+1)
                return memory[(i,j)]
            memory[(i,j)] = False
            return False 
            
            
        memory = {}
        return recursiveMatch(0, 0)
        