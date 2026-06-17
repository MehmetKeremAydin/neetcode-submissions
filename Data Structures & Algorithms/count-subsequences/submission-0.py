class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def recursiveSearch(str1: str, str2: str) -> int:
            if (str1, str2) in memory: return memory[(str1, str2)]
            if str2 == "":
                return 1
            idx = str1.find(str2[0])
            if idx == -1:
                return 0
            option1 = recursiveSearch(str1[(idx+1):], str2[1:])
            option2 = recursiveSearch(str1[(idx+1):], str2)
            memory[(str1, str2)] = option1 + option2
            return option1 + option2
            
        memory = {}
        return recursiveSearch(s, t)