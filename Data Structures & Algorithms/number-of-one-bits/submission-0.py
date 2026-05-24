class Solution:
    def hammingWeight(self, n: int) -> int:
        zeroCount = 0
        while n > 0:
            if n % 2 == 1:
                zeroCount += 1
            n //=2
        return zeroCount
        