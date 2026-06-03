class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hist ={}
        n = len(nums)
        for num in nums:
            hist[num] = hist.get(num, 0) + 1
            if hist[num] > n//2:
                return num
        return -1
        