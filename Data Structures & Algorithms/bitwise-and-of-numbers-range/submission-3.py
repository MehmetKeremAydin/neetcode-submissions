class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        result = 0
        dist = right - left
        cR, cL = left, right
        rL, rR = 0, 0
        for i in range(32):
            if 2**i < dist:
                cL //= 2
                cR //= 2
            else:
                rL = cL % 2
                rR = cR % 2
                cL //= 2
                cR //= 2 
            print(i, cR, cL, rR, rL)
            if rL == 1 and rR == 1:
                result += 1 << i
        return result