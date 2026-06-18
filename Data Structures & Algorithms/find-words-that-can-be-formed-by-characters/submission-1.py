class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hist = {}
        for char in chars:
            hist[char] = hist.get(char, 0) + 1
        count = 0
        for word in words:
            possible = True
            curHist = hist.copy()
            for i, char in enumerate(word):
                if char in curHist and curHist[char] > 0:
                    curHist[char] -= 1
                else:
                    possible = False
                    break
            if possible:
                count += len(word)
        return count