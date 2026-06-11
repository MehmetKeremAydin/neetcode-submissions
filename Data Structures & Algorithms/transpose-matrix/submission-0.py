class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        h, w = len(matrix), len(matrix[0])
        newMatrix = []
        for i in range(w):
            newMatrix.append([0]*h)
        for i in range(h):
            for j in range(w):
                newMatrix[j][i] = matrix[i][j]
        return newMatrix
        