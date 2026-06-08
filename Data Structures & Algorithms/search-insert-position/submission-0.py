class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        i = 0
        if target < nums[left]:
            return 0
        elif target > nums[right]:
            return len(nums)
        while right - left > 1:
            i += 1
            if i == 20:
                break
            center = (left+right)//2
            print(left, right, center)
            if target < nums[center]:
                right = center
            elif target > nums[center]:
                left = center
            else:
                return center
        return right