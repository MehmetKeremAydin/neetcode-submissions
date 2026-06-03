class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        histT = [0] * 26
        histS = [0] * 26
        for charS, charT in zip(s, t):
            histT[ord(charT)-ord('a')] += 1
            histS[ord(charS)-ord('a')] += 1
        return True if histT == histS else False