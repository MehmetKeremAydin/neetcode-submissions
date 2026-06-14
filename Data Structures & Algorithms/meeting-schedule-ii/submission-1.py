"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals = sorted(intervals, key = lambda x:x.start)
        endsCounter = {}
        maxOverlap = 1
        for i in range(len(intervals)):
            curBegin, curEnd = intervals[i].start, intervals[i].end
            curOverlap = 1
            toBeRemoved = set()
            for end in endsCounter:
                if end > curBegin:
                    curOverlap += endsCounter[end]
                else:
                    toBeRemoved.add(end)
            while toBeRemoved:
                endsCounter.pop(toBeRemoved.pop())
            endsCounter[curEnd] = endsCounter.get(curEnd, 0) + 1
            maxOverlap = max(maxOverlap, curOverlap)
        return maxOverlap