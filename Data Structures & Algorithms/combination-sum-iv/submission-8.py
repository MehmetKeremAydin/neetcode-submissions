class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def countPerms(cnts):
            elemCount = 0
            div = 1
            for count in cnts:
                elemCount += count
                div *= math.factorial(count)
            return int(math.factorial(elemCount) / div)
        
        def recursiveSearch(i, curSum, curState):
            if curSum == target:
                nonlocal count
                count += countPerms(curState)
                return
            if curSum > target or i == len(nums):
                return
            curState[i] += 1
            recursiveSearch(i, curSum + nums[i], curState)
            curState[i] -= 1
            recursiveSearch(i+1, curSum, curState)
            
        memory = set()
        count = 0
        state = [0]*len(nums)
        recursiveSearch(0, 0, state)
        return count