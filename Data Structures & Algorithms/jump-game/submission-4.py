class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curEnergy = 0
        for i in range(len(nums)-1):
            curEnergy = max(nums[i], curEnergy-1)
            if curEnergy <= 0:
                return False
        return True
        