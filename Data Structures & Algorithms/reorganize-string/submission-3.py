class Solution:
    def reorganizeString(self, s: str) -> str:
        hist = {}
        for char in s:
            hist[char] = hist.get(char, 0) + 1
        heap = [(value, key) for key, value in hist.items()]
        heapq.heapify_max(heap)
        if 2 * heap[0][0] > len(s) + 1:
            return ""
        answer = ""
        prevFreq, prevLetter = None, None
        while heap:
            freq, letter = heapq.heappop_max(heap)
            answer += letter
            if prevLetter != None and prevFreq > 1:
                heapq.heappush_max(heap, (prevFreq-1, prevLetter))
            prevFreq, prevLetter = freq, letter
        if prevFreq > 1:
            answer += prevLetter
        return answer
            