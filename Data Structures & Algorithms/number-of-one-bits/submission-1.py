class Solution:
    def hammingWeight(self, n: int) -> int:
        zeroCount = 0
        while n :
            if n % 2 == 1:
                zeroCount += 1
            n = n >> 1
        return zeroCount
        