class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        iterCount = min(len(word1), len(word2))
        for i in range(iterCount):
            ans = ans + word1[i] + word2[i]
        if len(word1) > len(word2):
            ans += word1[iterCount:]
        elif len(word2) > len(word1):
            ans += word2[iterCount:]
        return ans
        