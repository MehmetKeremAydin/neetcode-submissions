class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            x, y = point
            dist2 = x**2 + y**2 
            if len(maxHeap) < k:
                heapq.heappush_max(maxHeap, (dist2, point))
            elif maxHeap[0][0] > dist2:
                heapq.heappop_max(maxHeap)
                heapq.heappush_max(maxHeap, (dist2, point))
            #print(maxHeap)
        answer = [data[1] for data in maxHeap]
        return answer
        