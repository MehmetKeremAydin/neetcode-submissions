class Solution:
    def buildTrie(self, words:list(str)) -> dict:
        trie = {}
        for word in words:
            cur = trie
            for i, char in enumerate(word):
                cur[char] = cur.get(char, [{}, False])
                if i == len(word)-1:
                    cur[char][1] = True
                cur = cur[char][0]
        return trie
    
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        def dfs(i):
            if i in memory:
                return memory[i]
            if i == len(s):
                return 0

            res = 1 + dfs(i + 1)
            cur = trie
            j = i
            while j < len(s) and s[j] in cur:
                if cur[s[j]][1]:
                    res = min(res, dfs(j + 1))
                cur = cur[s[j]][0]
                j += 1
            memory[i] = res
            return res

        trie = self.buildTrie(dictionary)
        memory = {}
        return dfs(0)
    
    
        