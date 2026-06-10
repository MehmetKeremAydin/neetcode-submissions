class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        if nums[r] > nums[l]:
            return nums[l]
        while r - l > 1:
            print(l,r)
            c = (r + l) // 2
            if nums[c] > nums[r]:
                l = c
            else:
                r = c
        return nums[r]


        