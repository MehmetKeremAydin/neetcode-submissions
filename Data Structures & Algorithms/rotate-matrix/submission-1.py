class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        h = len(matrix)
        half1 = h//2+1 if h%2 else h//2
        half2 = h//2
        t = h - 1 
        for i in range(half1):
            for j in range(half2):
                temp = matrix[i][j]
                matrix[i]  [j]     = matrix[t-j][i]
                matrix[t-j][i]     = matrix[t-i][t-j]
                matrix[t-i][t-j]   = matrix[j]  [t-i]
                matrix[j]  [t-i]   = temp

        