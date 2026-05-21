class Solution:
    def getNext(self, n):
        nStr = str(n)
        total = 0
        for char in nStr:
            total += int(char)**2
        return total;
    
    def isHappy(self, n: int) -> bool:
        fast = n
        slow = n
        while(fast != 1):
            slow = self.getNext(slow)
            fast = self.getNext(fast)
            fast = self.getNext(fast)
            if slow == fast and fast != 1:
                return False       
        return True