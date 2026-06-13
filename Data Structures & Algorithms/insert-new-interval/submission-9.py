class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeOverlapping(inter1, inter2):
            left = min(inter1[0], inter2[0])
            right = max(inter1[1], inter2[1])
            return (left, right)
        answer = []
        for i, inter in enumerate(intervals):
            if newInterval[0] > inter[1]:
                answer.append(inter)
            elif newInterval[1] < inter[0]:
                inserted = i
                answer.append(newInterval)
                return answer + intervals[i:]
            else:
                newInterval = mergeOverlapping(newInterval, inter)
        answer.append(newInterval)
        return answer
