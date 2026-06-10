class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        data = [(a, 'a'), (b, 'b'), (c, 'c')]
        heap = []
        for entry in data:
            if entry[0] > 0:
                heapq.heappush_max(heap, (entry[0], entry[1]))
        totalBudget = a + b + c
        useDouble = None
        if 2*a > totalBudget+1:
            useDouble = 'a'
        elif 2*b > totalBudget+1:
            useDouble = 'b'
        elif 2*c > totalBudget+1:
            useDouble = 'c'
        prevCount, prevChar = 0, None
        answer = ""
        while heap:
            count, char = heapq.heappop_max(heap)
            if char == useDouble and count > 1:
                answer += 2*char
                count -= 2
            elif count > 0:
                answer += char
                count -= 1
            if prevCount > 0:
                heapq.heappush_max(heap, (prevCount, prevChar))
            prevCount, prevChar = count, char
            #print(answer, heap)
        return answer