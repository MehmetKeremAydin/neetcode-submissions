class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        maxPal = ""
        for i in range(2*len(s)-1):
            if i % 2 == 0:
                left, right = i//2, i//2
            else:
                left, right = i//2, i//2+1
            while left>=0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            curLen = right-left-1
            if curLen > maxLen:
                maxLen = curLen
                maxPal = s[(left+1):right]
        return maxPal
        