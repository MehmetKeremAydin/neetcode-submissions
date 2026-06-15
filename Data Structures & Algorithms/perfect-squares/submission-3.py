class Solution:
    def numSquares(self, n: int) -> int:
        def recursiveSearch(target):
            if target in memory:
                return memory[target]
            if target == 0:
                return 0
            if target < 0:
                return math.inf
            minNumbOfComp = math.inf
            for i in range(len(nums)):
                res = recursiveSearch(target-nums[i])
                minNumbOfComp = min(res+1, minNumbOfComp)
            memory[target] = minNumbOfComp
            return minNumbOfComp
        
        memory = {}
        nums = []
        i = 1
        while i**2 <= n:
            nums.append(i**2)
            i += 1
        nums = nums[::-1]
        return recursiveSearch(n)
        

        