class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        end = len(nums) - 1
        for i in range(end-1, -1, -1):
            if i + nums[i] >= end:
                nums[i] = 1
                continue
            if nums[i] == 0:
                nums[i] = 99999
                continue
            nums[i] = min(nums[(i+1):min((nums[i]+i+1), end)]) + 1
            print(nums[-5:])
        return nums[0]



        