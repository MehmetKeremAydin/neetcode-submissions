class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)-1
        while l <= r:
            c = (l+r) // 2
            if nums[c] == target:
                return True
            if nums[l] < nums[c]:
                if nums[l] <= target < nums[c]:
                    r = c - 1
                else:
                    l = c + 1
            elif nums[l] > nums[c]:
                if nums[c] < target <= nums[r]:
                    l = c + 1
                else:
                    r = c - 1
            else:
                l += 1
        return False