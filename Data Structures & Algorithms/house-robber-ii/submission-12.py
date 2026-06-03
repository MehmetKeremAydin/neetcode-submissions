class Solution:
    def rob(self, nums: List[int]) -> int:
        def buildSoln(nums):
            if len(nums) == 1:
                return nums[0]
            left, right = 0, nums[0]
            for i in range(1,len(nums)):
                temp = left + nums[i]
                left = right
                right = max(right, temp)
            return right
        
        if len(nums) == 1:
            return nums[0]
        skippedFirst = buildSoln(nums[1:])
        robbedFirst = buildSoln(nums[:-1])
        return max(skippedFirst, robbedFirst)
        