class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lenStartAtIdx = [1] * len(nums)
        lenStartAtIdx[-1] = 1
        maxLen = 0
        for i in reversed(range(len(nums))):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    lenStartAtIdx[i] = max(1, lenStartAtIdx[i], lenStartAtIdx[j]+1)
            maxLen = max(maxLen, lenStartAtIdx[i])
        return maxLen

        