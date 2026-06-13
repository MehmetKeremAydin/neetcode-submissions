class Solution:
    def totalNQueens(self, n: int) -> int:
        def updateBoard(board, row, col):
            newBoard = [[False]*n] * row
            for i in range(row, n):
                newBoard.append(board[i].copy())
                newBoard[i][col] = False
                c1, c2 = col+(i-row), col-(i-row)
                if 0<=c1<n:
                    newBoard[i][c1] = False
                if 0<=c2<n:
                    newBoard[i][c2] = False
            return newBoard

        def recursiveSearch(i, board):
            if i == n:
                nonlocal answerCount
                answerCount += 1
                return
            if not all(board[i] for i in range(n)):
                return
            for j in range(n):
                if not board[i][j]:
                    continue
                newBoard = updateBoard(board, i, j)
                #print(i,j, newBoard)
                recursiveSearch(i+1, newBoard)
        
        answerCount = 0
        validLocations = [[True]*n]*n
        recursiveSearch(0, validLocations)
        return answerCount