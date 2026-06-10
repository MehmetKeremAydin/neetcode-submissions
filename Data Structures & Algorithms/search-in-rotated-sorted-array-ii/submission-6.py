class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def regularBS(start, end):
            l, r = start, end
            while l<=r:
                c = (l + r) // 2
                if nums[c] < target:
                    l = c + 1
                elif nums[c] > target:
                    r = c - 1
                else:
                    return True
            return True if target == nums[l] else False
        
        l, r = 0, len(nums)-1
        while l<=r:
            c = (l + r) // 2
            if nums[c] == target:
                return True
            elif nums[l] < nums[c]:
                if nums[l] <= target <= nums[c]:
                    return regularBS(l, c)
                else:
                    l=c+1
            elif nums[l] > nums[c]:
                if nums[c] <= target <= nums[r]:
                    return regularBS(c, r)
                else:
                    r=c-1
            else:
                l += 1
        return False