class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h = len(matrix)
        w = len(matrix[0])
        firstRowZero = True if 0 in matrix[0] else False
        firstColZero = False
        for i in range(h):
            if matrix[i][0] == 0:
                firstColZero = True
                break
        for i in range(1,h):
            for j in range(1,w):
                if (matrix[i][j] == 0):
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1,h):
            if matrix[i][0] == 0:
                for j in range(w):
                    matrix[i][j] = 0
        for j in range(1,w):
            if matrix[0][j] == 0:
                for i in range(h):
                    matrix[i][j] = 0
        if firstRowZero:
            for j in range(w):
                    matrix[0][j] = 0
        if firstColZero:
            for i in range(h):
                    matrix[i][0] = 0


        
        