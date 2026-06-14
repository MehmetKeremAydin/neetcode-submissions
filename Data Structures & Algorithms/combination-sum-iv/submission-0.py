class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def countPerms(state):
            elemCount = 0
            div = 1
            for key in state:
                elemCount += state[key]
                div *= math.factorial(state[key])
            return int(math.factorial(elemCount) / div)
        
        def recursiveSearch(i, curSum, curState):
            #print(i, curSum)
            if curSum == target:
                nonlocal count
                count += countPerms(curState)
                return True
            if curSum > target or i == len(nums):
                return False
            curState[nums[i]] += 1
            recursiveSearch(i, curSum + nums[i], curState)
            curState[nums[i]] -= 1
            recursiveSearch(i+1, curSum, curState)
        
        count = 0
        state = {key:0 for key in nums}
        recursiveSearch(0, 0, state)
        return count