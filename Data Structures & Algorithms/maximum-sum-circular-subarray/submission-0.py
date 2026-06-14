class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curMaxSum = curMinSum = globalMaxSum = globalMinSum = total = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            curMaxSum = max(curMaxSum + num, num)
            curMinSum = min(curMinSum + num, num)
            globalMaxSum = max(globalMaxSum, curMaxSum)
            globalMinSum = min(globalMinSum, curMinSum)
            total += num
        return max(globalMaxSum, total - globalMinSum) if any(i > 0 for i in nums) else globalMaxSum           