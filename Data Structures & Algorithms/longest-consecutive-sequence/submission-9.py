class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums = set(nums)
        maxLen = 1
        for num in nums:
            if num-1 in nums:
                continue
            else:
                curNum = num
                curLen = 0
                while curNum in nums:
                    curNum += 1
                    curLen += 1
                maxLen = max(maxLen, curLen)
        return maxLen