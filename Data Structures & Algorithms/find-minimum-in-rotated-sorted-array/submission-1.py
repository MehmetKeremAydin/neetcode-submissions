class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            cur = (l + r) // 2
            if nums[l] <= nums[cur] and nums[cur] <= nums[r]:
                return nums[l]
            if(nums[l] < nums[cur]):
                l = cur + 1
            elif (nums[l] > nums[cur]):
                l += 1
                r = cur
            else:
                return nums[r]
            print("l: ", l, nums[l], ' r:', r, nums[r])
        return nums[l]                

        