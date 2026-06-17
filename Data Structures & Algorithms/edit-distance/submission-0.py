class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def recursiveSearch(str1:str, str2:str) -> int:
            if (str1, str2) in memory: return memory[(str1, str2)]
            if str1 == str2:
                return 0
            if str1 == "":
                return len(str2)
            if str2 == "":
                return len(str1)
            if str1[0] == str2[0]:
                return recursiveSearch(str1[1:], str2[1:])
            optionReplace = recursiveSearch(str1[1:], str2[1:]) + 1
            optionDelete = recursiveSearch(str1[1:], str2) + 1
            optionInsert = recursiveSearch(str1, str2[1:]) + 1
            memory[(str1, str2)] = min(optionReplace, optionDelete, optionInsert)
            return min(optionReplace, optionDelete, optionInsert)
        memory = {}
        return recursiveSearch(word1, word2)

            

        