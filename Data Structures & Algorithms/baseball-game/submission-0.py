class Solution:
    def calPoints(self, operations: List[str]) -> int:
        arr = []
        for ops in operations:
            if ops == "+":
                arr.append(arr[-1] + arr[-2])
            elif ops == "D":
                arr.append(2*arr[-1])
            elif ops == "C":
                arr.pop()
            else:
                arr.append(int(ops))
        return sum(arr)
        