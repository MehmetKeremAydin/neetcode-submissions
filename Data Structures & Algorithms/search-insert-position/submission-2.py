class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r= 0, len(nums) - 1
        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            elif nums[c] < target:
                memory = c + 1
                l = c + 1
            else:
                memory = c
                r = c - 1
        return memory