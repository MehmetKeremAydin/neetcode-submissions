class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i, num in enumerate(nums):
            while 0<num<=n and num != i+1 and nums[num-1] != nums[i]:
                nums[i], nums[num-1] = nums[num-1], nums[i]
                num = nums[i]
        for i in range(n):
            if nums[i] != i+1:
                return i+1
        return n+1    