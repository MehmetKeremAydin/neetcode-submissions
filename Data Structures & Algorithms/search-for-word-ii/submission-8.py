class Trie:
    def __init__(self):
        self.prefix = [{}, None]
    
    def insert(self, word:str) -> None:
        cursor = self.prefix[0]
        for i, char in enumerate(word):
            cursor.setdefault(char, [{}, None])
            if i == len(word)-1:
                cursor[char][1] = word
            cursor = cursor[char][0]

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(head:list, i:int, j:int, curAns:set, seen:set) -> set:
            #print(i,j, curAns)
            if head[1] != None:
                curAns.add(head[1])
            if 0<=i<h and 0<=j<w and board[i][j] in head[0] and not (i,j) in seen:
                #print(head, i, j)
                for dirc in dircList:
                    r,c = i + dirc[0], j + dirc[1]
                    seen.add((i,j))
                    dfs(head[0][board[i][j]], r, c, curAns, seen)
                    seen.discard((i,j))
            return curAns
                         
        trie = Trie()
        for word in words:
            trie.insert(word)
        h = len(board)
        w = len(board[0])
        answer = set()
        dircList = [[1,0], [-1, 0], [0,1], [0,-1]]
        for i, row in enumerate(board):
            for j, entry in enumerate(row):
                cursor = trie.prefix
                curAnswer = set()
                seen = set()
                found = dfs(cursor, i, j, curAnswer, seen)
                if found:
                    answer = answer.union(found)
        return list(answer)