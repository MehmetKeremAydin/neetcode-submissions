class Solution:
    def buildTrie(self, words:list) -> dict:
        Trie = [{}, False] 
        for word in words:
            cur = Trie[0]
            for i, char in enumerate(word):
                cur[char] = cur.get(char, [{}, False])
                if i == len(word) - 1:
                    cur[char][1] = True
                cur = cur[char][0]
        return Trie
        
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def recursiveSearch(i, curTrie, curSent):
            #print(i, curSent)
            gapIdx = curSent.rfind(" ")
            curWord = curSent if gapIdx == -1 else curSent[gapIdx:]
            if (i, curWord) in deadEnds:
                return False 
            if i == len(s):
                if curTrie[1]:
                    answer.append(curSent)
                return
            if not s[i] in curTrie[0]:
                deadEnds.add((i, curWord))
                return
            nextTrie = curTrie[0][s[i]]
            curSent += s[i]
            if nextTrie[1] and i != len(s) - 1:
                curSentWSpace = curSent + " "
                recursiveSearch(i+1, trie, curSentWSpace)
            recursiveSearch(i+1, nextTrie, curSent)
            

        deadEnds = set()
        answer = []
        trie = self.buildTrie(wordDict)
        #print(trie)
        recursiveSearch(0, trie, "")
        return answer