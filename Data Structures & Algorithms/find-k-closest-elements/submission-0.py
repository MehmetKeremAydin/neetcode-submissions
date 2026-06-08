class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        max_heap = []
        for num in arr:
            dist = abs(num-x)
            if len(max_heap) < k:
                heapq.heappush_max(max_heap, (dist, num))
            elif max_heap[0] > (dist, num):
                heapq.heappush_max(max_heap, (dist, num))
                heapq.heappop_max(max_heap)
        answer = [i[1] for i in max_heap]
        answer = sorted(answer)
        return answer
        