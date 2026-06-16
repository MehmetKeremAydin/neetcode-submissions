class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def recursiveSearch(i, target):
            if (i, target) in memory: return memory[(i, target)]
            if i == len(nums): 
                if target == 0:
                    return 1
                else:
                    return 0
            count1 = recursiveSearch(i+1, target + nums[i])
            count2 = recursiveSearch(i+1, target - nums[i])
            memory[(i, target)] = count1 + count2
            return count1 + count2
        
        memory = {}
        return recursiveSearch(0, target)