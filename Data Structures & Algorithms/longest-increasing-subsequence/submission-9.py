class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nNums = len(nums)
        def recursiveSearch(startIdx, prevNum):
            if startIdx in memory:
                return memory[startIdx]
            maxLen = 0
            if startIdx == nNums:
                return maxLen
            for idx in range(startIdx, nNums):
                if nums[idx] > prevNum:
                    if (prevNum, idx) in memory:
                        curLen = memory[prevNum, idx]
                    else:
                        curLen = recursiveSearch(idx+1, nums[idx]) + 1
                        memory[prevNum, idx] = curLen
                    maxLen = max(curLen, maxLen)
            memory[startIdx] = maxLen
            return maxLen
        memory = {}   

        
        return recursiveSearch(0, -math.inf)
        