class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = -1001
        curSum = 0
        for num in nums:
            curSum += num
            best = max(best, curSum)
            if curSum < 0:
                curSum = 0
        return best

        