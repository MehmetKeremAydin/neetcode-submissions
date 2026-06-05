class Solution:
    def reverse(self, x: int) -> int:
        num = 0
        sign = -1 if x<0 else 1
        x = abs(x)
        while x != 0:
            num *= 10
            num += x % 10 if x > 0 else 10 - (x % 10)
            x = x//10
        return int(sign*num) if num < 2**31-1 else 0