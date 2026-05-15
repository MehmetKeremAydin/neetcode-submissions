class Solution:
    def bsearch(self, nums: List[int], target: int, left:int, right:int) -> int:
        while (left<=right):
            mid = (left + right) // 2
            if target == nums[mid]: 
                return mid
            elif target < nums[mid]:
                right = mid - 1;
            else:
                left = mid + 1
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while(l <= r) :
            m = (l + r) // 2
            if nums[l] <= nums[m] and nums[m] <= nums[r]:
                return self.bsearch(nums, target, l, r)
            elif nums[l] <= nums[m]:
                if nums[l] <= target <= nums[m]:
                    return self.bsearch(nums, target, l, m)
                else:
                    l = m + 1;
            elif nums[m] <= nums[r]:
                if nums[m] <= target <= nums[r]:
                    return self.bsearch(nums, target, m, r)
                else:
                    r = m - 1;
        return -1