class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def mergeOverlapping(inter1, inter2):
            left = min(inter1[0], inter2[0])
            right = max(inter1[1], inter2[1])
            return (left, right)
        answer = []
        inserted = None
        for i, inter in enumerate(intervals):
            if inserted != None:
                break
            if newInterval[0] > inter[1]:
                answer.append(inter)
                continue
            elif newInterval[1] < inter[0]:
                inserted = i
                answer.append(newInterval)
                answer.append(inter)
                continue
            else:
                newInterval = mergeOverlapping(newInterval, inter)
                continue
        if inserted == None:
            answer.append(newInterval)
        else:
            answer += intervals[(inserted+1):]
        return answer
