class Solution:
    def generateWordTree(self, words:list) -> dict:
        wordTree = [dict(), False]
        for word in words:
            cursor = wordTree[0]
            for i, char in enumerate(word):
                cursor.setdefault(char, [{}, False])
                if i == len(word) - 1:
                    cursor[char][1] = True
                cursor = cursor[char][0]
        return wordTree

    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def recursiveSearch(s):
            if s in memory:
                return False
            if s == "":
                return True
            cursor = wordTree[0]
            for i, char in enumerate(s):
                if char in cursor:
                    if cursor[char][1] == True:
                        found = recursiveSearch(s[(i+1):])
                        if found:
                            return True
                    cursor = cursor[char][0]
                else:
                    memory.add(s)
                    return False
            memory.add(s)
            return False
                
        memory = set()   
        wordSet = set(wordDict)
        wordTree = self.generateWordTree(wordDict)

        return recursiveSearch(s)
        