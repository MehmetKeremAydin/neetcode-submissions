class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        rollHist = {}
        mostFrequenctChar = None
        topFreq = -1
        l = 0
        windowSize = 0
        for r,c in enumerate(s):
            rollHist[c] = rollHist.get(c, 0) + 1
            if rollHist[c] > topFreq:
                topFreq = rollHist[c]
                mostFrequenctChar = c
            nontopFreqCount = r - l + 1 - topFreq
            while nontopFreqCount > k:
                rollHist[s[l]] -= 1
                if s[l] == mostFrequenctChar:
                    mostFrequenctChar = max(rollHist, key = lambda x: rollHist[x])
                    topFreq = rollHist[mostFrequenctChar]
                l += 1
                nontopFreqCount = r - l + 1 - topFreq
            windowSize = max(windowSize, r-l+1)
        return windowSize