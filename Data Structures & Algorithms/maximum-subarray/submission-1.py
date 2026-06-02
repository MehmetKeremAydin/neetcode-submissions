class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        curSum = 0
        for num in nums:
            curSum += num
            best = max(best, curSum)
            curSum = max(0, curSum)
        return best

        