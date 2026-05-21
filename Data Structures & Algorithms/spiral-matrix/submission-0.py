class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dir = 0
        h = len(matrix)
        w = len(matrix[0])
        size = h*w
        count = 0
        i,j = 0,0
        answer = list()
        layer = 0
        while True:
            answer.append(matrix[i][j])
            count += 1
            if count == size:
                return answer
            if dir == 0 and j == w-layer-1:
                dir = 1
            elif dir == 1 and i == h-layer-1:
                dir=2
            elif dir == 2 and j == layer:
                dir=3
                layer += 1
            elif dir == 3 and i == layer:
                dir = 0
            
            if dir == 0:
                j += 1
            elif dir == 1:
                i += 1
            elif dir == 2:
                j -= 1
            elif dir == 3:
                i -= 1



        