class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        inp = []
        out = []
        for trip in trips:
            heapq.heappush(inp, (trip[1], trip[0]))
            heapq.heappush(out, (trip[2], trip[0]))
        curPop = 0
        while inp:
            if inp[0][0] < out[0][0]:
                dist, pop = heapq.heappop(inp)
                curPop += pop
            else:
                dist, pop = heapq.heappop(out)
                curPop -= pop
            if curPop > capacity:
                return False
        return True
        