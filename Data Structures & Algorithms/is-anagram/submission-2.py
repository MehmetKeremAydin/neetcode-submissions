class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hist = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            hist[ord(s[i]) - ord('a')]+=1;
            hist[ord(t[i]) - ord('a')]-=1;
        if hist.count(0) != 26:
            return False
        else:
            return True
        
        