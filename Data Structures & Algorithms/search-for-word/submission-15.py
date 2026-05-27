class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def searchAdj(curLetterIdx: int, hIdx:int, wIdx:int):
            #print(curLetterIdx, hIdx, wIdx)
            if curLetterIdx == len(word):
                return True
            else:
                foundUp, foundDown, foundR, foundL = False, False, False, False
                board[hIdx][wIdx] = None
                if hIdx - 1 >= 0 and board[hIdx - 1][wIdx] == word[curLetterIdx]:
                    foundUp = searchAdj(curLetterIdx+1, hIdx-1, wIdx)
                if hIdx + 1 < h and board[hIdx + 1][wIdx] == word[curLetterIdx]:
                    foundDown = searchAdj(curLetterIdx+1, hIdx+1, wIdx)
                if wIdx + 1 < w and board[hIdx][wIdx+1] == word[curLetterIdx]:
                    foundR = searchAdj(curLetterIdx+1, hIdx, wIdx+1)
                if wIdx - 1 >= 0 and board[hIdx][wIdx-1] == word[curLetterIdx]:
                    foundL = searchAdj(curLetterIdx+1, hIdx, wIdx-1)
                board[hIdx][wIdx] = word[curLetterIdx-1]
                return foundUp or foundDown or foundR or foundL
        h, w = len(board), len(board[0])
        initL = word[0]
        found = False
        for i in range(h):
            for j in range(w):
                if board[i][j] == initL:
                    found = searchAdj(1, i, j)
                    if found:
                        return True
        return False 
        