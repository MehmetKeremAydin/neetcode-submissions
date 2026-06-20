class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):
            if 0<nums[i]<=len(nums) and nums[i] != i+1 and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        for i, n in enumerate(nums):
            if i+1 != n:
                return i+1
        return nums[-1]+1
