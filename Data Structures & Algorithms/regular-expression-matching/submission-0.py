class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def recursiveMatch(i:int, j:int) -> bool:
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                return recursiveMatch(i,j+2) or (match and recursiveMatch(i+1, j))
            if match:
                return recursiveMatch(i+1, j+1)
            return False 
            
            

        return recursiveMatch(0, 0)
        