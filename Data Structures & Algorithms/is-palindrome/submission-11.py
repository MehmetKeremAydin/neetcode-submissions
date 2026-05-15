class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while (left<right):
            while(not s[right].isalnum() and right > 0):
                right -= 1
            while(not s[left].isalnum() and left < len(s)-1):
                left += 1
            if left >= right:
                return True
            print('Left: ', s[left], ' Right: ', s[right])
            if(s[right].casefold() != s[left].casefold()):
                return False
            right -= 1
            left += 1
        return True