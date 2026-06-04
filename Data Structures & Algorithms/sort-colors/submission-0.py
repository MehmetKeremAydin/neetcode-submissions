class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hist = [0] * 3
        for num in nums:
            hist[num] += 1
        for i in range(hist[0]):
            nums[i] = 0
        for i in range(hist[0], hist[0]+hist[1]):
            nums[i] = 1
        for i in range(hist[0]+hist[1], len(nums)):
            nums[i] = 2