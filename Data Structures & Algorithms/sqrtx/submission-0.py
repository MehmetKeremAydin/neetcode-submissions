class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, 2**16
        while l<=r:
            c = (l + r) // 2
            sq = c*c
            print(l, r, c, sq)
            if sq == x:
                return c
            elif sq < x:
                mem = c
                l = c + 1
            else:
                mem = c - 1
                r = c - 1
        return mem
        