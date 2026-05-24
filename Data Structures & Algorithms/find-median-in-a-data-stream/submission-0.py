class MedianFinder:

    def __init__(self):
        self.lowerHalf = [] #maxHeap (Bias)
        self.upperHalf = [] #minHeap
        self.numCount = 0

    def addNum(self, num: int) -> None:
        if self.numCount == 0:
            heapq.heappush(self.upperHalf, num)
            self.numCount += 1
            return
        elif self.numCount == 1:
            if num <= self.upperHalf[0]:
                heapq.heappush_max(self.lowerHalf, num)
            else:
                heapq.heappush(self.upperHalf, num)
                heapq.heappush_max(self.lowerHalf, heapq.heappop(self.upperHalf))
            self.numCount += 1
            return
        else:
            if num<self.lowerHalf[0]:
                heapq.heappush_max(self.lowerHalf, num)
            else:
                heapq.heappush(self.upperHalf, num)
            self.numCount += 1
            if (len(self.upperHalf) - len(self.lowerHalf) > 1):
                heapq.heappush_max(self.lowerHalf, heapq.heappop(self.upperHalf))
            elif( len(self.upperHalf) < len(self.lowerHalf)):
                heapq.heappush(self.upperHalf, heapq.heappop_max(self.lowerHalf))
        return

    def findMedian(self) -> float:
        if self.numCount % 2 == 0:
            return (self.upperHalf[0] + self.lowerHalf[0]) / 2
        else:
            return self.upperHalf[0]
        
        