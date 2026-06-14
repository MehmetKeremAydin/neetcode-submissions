class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        queriesS = sorted(queries)
        intervals = sorted(intervals)
        itrQ = itrInter = 0
        heap = []
        answer = {}
        while itrQ < len(queriesS):
            quer = queriesS[itrQ]
            while itrInter < len(intervals) and intervals[itrInter][0] <= quer:
                curBegin, curEnd = intervals[itrInter]
                heapq.heappush(heap, (curEnd-curBegin + 1, curEnd))
                itrInter += 1
            while heap and heap[0][1] < quer:
                heapq.heappop(heap)
            if heap:
                answer[quer] = heap[0][0]
            else:
                answer[quer] = -1
            itrQ += 1
        result = [answer[i] for i in queries]
        return result