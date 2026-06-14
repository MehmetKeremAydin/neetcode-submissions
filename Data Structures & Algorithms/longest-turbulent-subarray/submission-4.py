class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        diff = [arr[i]-arr[i-1] for i in range(1,len(arr))]
        maxSize = min(2, len(arr))
        if len(arr) <= 2:
            return 1 if len(arr) == 1 or arr[0] == arr[1] else 2
        if all(x == 0 for x in diff):
            return 1
        curSize = 2
        for i in range(1, len(diff)):
            print(i, curSize)
            if diff[i] * diff[i-1] >= 0:
                curSize = 2
                continue
            curSize += 1
            maxSize = max(maxSize, curSize)
        return maxSize
        