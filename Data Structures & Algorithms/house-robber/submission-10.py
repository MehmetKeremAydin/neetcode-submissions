class Solution:
    def rob(self, nums: List[int]) -> int:
        left, right = 0, 0
        for num in nums:
            best = max(num+left, right)
            left = right
            right = best
        return best