class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        h = len(matrix)
        w = len(matrix[0])
        l, r = 0, h*w-1
        while(l <= r):
            cur = (l + r) // 2
            ch = cur // w
            cw = cur % w
            if matrix[ch][cw] == target:
                return True
            elif matrix[ch][cw] < target:
                l = cur + 1
            else:
                r = cur - 1
        return False



        