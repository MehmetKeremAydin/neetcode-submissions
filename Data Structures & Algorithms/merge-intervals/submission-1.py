class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def addToAnswer(sortedInters, newInterval):
            result = []
            for i in range(len(sortedInters)):
                if newInterval[0] > sortedInters[i][1]:
                    result.append(sortedInters[i])
                elif newInterval[1] < sortedInters[i][0]:
                    result.append(newInterval)
                    return result + sortedInters[i:]
                else:
                    newInterval = [min(sortedInters[i][0], newInterval[0]), max(sortedInters[i][1], newInterval[1])]
            result.append(newInterval)
            return result

        answer = [intervals[0]]
        for i in range(1, len(intervals)):
            answer = addToAnswer(answer, intervals[i])
        return answer
        