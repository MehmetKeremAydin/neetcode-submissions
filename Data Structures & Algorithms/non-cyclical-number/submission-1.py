class Solution:
    def isHappy(self, n: int) -> bool:
        seenBefore = set()
        total = n
        while(total!=1):
            totalStr = str(total)
            total = 0
            for char in totalStr:
                total += int(char)**2
            if total in seenBefore:
                return False
            else:
                seenBefore.add(total)
        return True