class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0
        for i in range(2*len(s)-1):
            left = i//2
            right = i//2 if i%2==0 else i//2+1
            while left>=0 and right<len(s) and s[left]==s[right]:
                counter += 1
                left -= 1
                right += 1
        return counter

        