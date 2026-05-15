class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()
        for i,num in enumerate(nums):
            if num in memory:
                return [memory[num], i]
            memory[target-num] = i
        