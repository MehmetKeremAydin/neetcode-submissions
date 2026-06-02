class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        cumProfit = [0] * len(nums)
        cumProfit[0] = nums[0]
        cumProfit[1] = nums[1]
        best = max(cumProfit[0], cumProfit[1])
        for i in range(2, len(nums)):
            cumProfit[i] = max(cumProfit[:(i-1)]) + nums[i]
            best = max(best, cumProfit[i])
        return best

        