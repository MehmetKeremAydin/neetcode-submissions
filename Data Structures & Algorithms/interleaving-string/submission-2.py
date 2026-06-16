class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        def recursiveSearch(s1:str, s2:str, target:str) -> bool:
            if(s1, s2) in memory:
                return False
            if s1 == "" and s2 == "" and target == "":
                return True
            result = False
            if len(s1) > 0 and len(target) > 0 and s1[0] == target[0]:
                result = recursiveSearch(s1[1:], s2, target[1:])
            if result: return True
            if len(s2) > 0 and len(target) > 0 and s2[0] == target[0]:
                result = recursiveSearch(s1, s2[1:], target[1:])
            if result: return result 
            memory.add((s1, s2))
            return False
       
        memory = set()
        return recursiveSearch(s1, s2, s3)
