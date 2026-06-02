class Solution:
    def rob(self, nums: List[int]) -> int:
        def recursiveSearch(toBeRobbed):
            n = len(toBeRobbed)
            if n in hashMap:
                return hashMap[n]
            if not toBeRobbed:
                return 0
            robbedHere = toBeRobbed.popleft()
            sumPassed = recursiveSearch(toBeRobbed.copy())
            if toBeRobbed:
                skipped = toBeRobbed.copy()
                skipped.popleft()
                sumRobbed = robbedHere + recursiveSearch(skipped)
            else:
                sumRobbed = robbedHere
            hashMap[n] = max(sumPassed, sumRobbed)
            return hashMap[n]

        hashMap = {}   
        queue = deque(nums)
        print(queue)
        maxProfit = recursiveSearch(queue)
        return maxProfit

        