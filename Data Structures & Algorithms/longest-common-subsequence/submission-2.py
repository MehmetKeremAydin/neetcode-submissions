class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recursiveSearch(baseText:str, longText:str) -> int:
            if (baseText, longText) in memory:
                return memory[(baseText, longText)]
            if baseText == "" or longText == "":
                return 0
            idx = longText.find(baseText[0])
            result1 = 0
            if idx != -1:
                result1 = recursiveSearch(baseText[1:], longText[(idx+1):]) + 1
            result2 = recursiveSearch(baseText[1:], longText)
            result = max(result1, result2)
            memory[(baseText, longText)] = result
            return result
        
        
        memory = {}
        if len(text1) <= len(text2): 
            baseText = text1
            longText = text2
        else: 
            baseText = text2
            longText = text1
        return recursiveSearch(longText, baseText)