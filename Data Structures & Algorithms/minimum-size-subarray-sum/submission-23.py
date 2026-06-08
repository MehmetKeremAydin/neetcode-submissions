class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        curSum = nums[0]
        minSize = len(nums)+1
        while True:
            if curSum < target and right < len(nums)-1:
                right += 1
                curSum += nums[right]
            elif curSum < target and right == len(nums)-1:
                break
            else:
                minSize = min(minSize, right-left+1)
                curSum -= nums[left]
                left += 1    
        return 0 if minSize == len(nums) + 1 else minSize