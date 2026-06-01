class Solution:
    def manhattanDist(self, str1:str, str2:str):
        diff = 0
        assert len(str1) == len(str2)
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                diff += 1
        return diff
    
    def isMDistOne(self, str1:str, str2:str):
        diff = 0
        assert len(str1) == len(str2)
        for char1, char2 in zip(str1, str2):
            if char1 != char2:
                diff += 1
            if diff > 1:
                return False
        return True if diff == 1 else False
    
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList.append(beginWord)
        adjMap = {word:[] for word in wordList}
        for word in wordList:
            for key in adjMap:
                if self.isMDistOne(word, key):
                    adjMap[key].append(word)
        # We start BFS
        seen = set()
        queue = deque()
        queue.append((beginWord, 1))
        seen.add(beginWord)
        while queue:
            curWord, curStep = queue.popleft()
            for edge in adjMap[curWord]:
                if edge == endWord:
                    return curStep + 1
                if not edge in seen:
                    queue.append((edge, curStep+1))
                    seen.add(edge)

        return 0

        