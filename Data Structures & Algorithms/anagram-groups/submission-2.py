class Solution:
    def word2hist(self, word : str):
        hist = [0]*26
        for letter in word:
            hist[ord(letter) - ord('a')] += 1
        return tuple(hist)
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = list()
        histTable = dict()
        for word in strs:
            hist = self.word2hist(word)
            if hist in histTable:
                idx = histTable[hist]
                answer[idx].append(word)
            else:
                histTable[hist] = len(answer)
                answer.append([word])
        return answer