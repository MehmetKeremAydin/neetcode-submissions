class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def recursiveSearch(target) -> int:
            if target in memory:
                return memory[target]
            if target == 0:
                return 1
            if target < 0:
                return 0
            count = 0
            for i in nums:
                count += recursiveSearch(target-i)
            memory[target] = count
            return count           
        memory = {}
        return recursiveSearch(target)

        