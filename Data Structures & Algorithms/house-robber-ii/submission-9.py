class Solution:
    def rob(self, nums: List[int]) -> int:
        def dfs(i, robbedFirst):
            if (i, robbedFirst) in memory:
                return memory[(i, robbedFirst)]
            if (i >= len(nums)) or (robbedFirst and i >= len(nums)-1):
                return 0
            memory[(i, robbedFirst)] = max(nums[i] + dfs(i+2, robbedFirst), dfs(i+1, robbedFirst))
            return memory[(i, robbedFirst)]
        memory = {}
        return max(nums[0]+dfs(2,True)  , dfs(1, False))
        