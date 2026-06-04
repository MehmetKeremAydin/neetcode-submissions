class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.matrix = matrix
        self.cumMatrix = [[0] * self.w for i in range(self.h)]
        for i, row in enumerate(matrix):
            rollingSum = 0
            for j, entry in enumerate(row):
                rollingSum = rollingSum + entry
                self.cumMatrix[i][j] = rollingSum
            if i > 0:
                for j in range(self.w):
                    self.cumMatrix[i][j] += self.cumMatrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        answer = self.cumMatrix[row2][col2]
        if row1 != 0:
            answer -= self.cumMatrix[row1-1][col2]
        if col1 != 0:
            answer -= self.cumMatrix[row2][col1-1]
        if col1 != 0 and row1 != 0:
            answer += self.cumMatrix[row1-1][col1-1]
        return answer

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)