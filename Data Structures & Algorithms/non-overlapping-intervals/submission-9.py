class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        prev = intervals[0]
        removalCount = 0
        for i in range(1, len(intervals)):
            if prev[1] <= intervals[i][0]:
                prev = intervals[i]
            else:
                removalCount += 1
                if prev[1] > intervals[i][1]:
                    prev = intervals[i]
        return removalCount

        