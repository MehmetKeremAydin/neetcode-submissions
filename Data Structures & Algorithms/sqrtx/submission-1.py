class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l<=r:
            c = (l + r) // 2
            sq = c*c
            if sq == x:
                return c
            elif sq < x:
                l = c + 1
            else:
                r = c - 1
        return l -1
        