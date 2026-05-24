class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        while n :
            if n % 2 == 1:
                oneCount += 1
            n = n >> 1
        return oneCount
        