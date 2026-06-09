# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            c = (l + r) // 2
            print(c)
            result = guess(c)
            if result == 0:
                return c
            elif result == -1:
                r = c - 1
            else:
                l = c + 1
        return -1 
        