class Solution:
    
    def validPalindrome(self, s: str) -> bool:
        def isPal(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
            check = isPal(left+1, right)
            if check:
                return True
            check = isPal(left, right-1)
            return check
        return True
            
            