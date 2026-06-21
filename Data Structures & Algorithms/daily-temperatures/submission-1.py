class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][1] > temp:
                stack.append((i, temp))
            else:
                while stack and stack[-1][1] < temp:
                    idx, _ = stack.pop()
                    answer[idx] = i - idx
                stack.append((i, temp))
        return answer