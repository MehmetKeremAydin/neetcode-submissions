class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderLUT = {}
        for i, char in enumerate(order):
            orderLUT[char] = i
        
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j = 0
            while j<len(word1) and j<len(word2) and word1[j] == word2[j]:
                j += 1
            if j == len(word1):
                continue
            elif j == len(word2) or orderLUT[word2[j]] < orderLUT[word1[j]]:
                return False
        return True