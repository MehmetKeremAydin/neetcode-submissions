class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def recursiveSearch(i, curSum, partitionCount):
            if (i, curSum) in memory:
                return memory[(i, curSum)]
            if partitionCount == k:
                memory[(i, curSum)] = True
                return True
            if curSum == partTotal:
                result = recursiveSearch(0, 0, partitionCount+1)
                if result:
                    memory[(i, curSum)] = True
                    return True
            if curSum > partTotal:
                memory[(i, curSum)] = False
                return False
            for i in range(len(nums)):
                if not usedNums[i] and curSum + nums[i] <= partTotal:
                    usedNums[i] = True
                    result = recursiveSearch(i+1, curSum + nums[i], partitionCount)
                    if result:
                        memory[(i, curSum)] = True
                        return True
                    usedNums[i] = False
            memory[(i, curSum)] = False
            return False
            

        usedNums = [False] * len(nums)
        memory = {}
        total = 0
        maxNum = 0
        nums = sorted(nums, reverse=True)
        for num in nums:
            maxNum = max(maxNum, num)
            total += num
        partTotal = total // k
        if partTotal * k != total or maxNum > partTotal or len(nums) < k:
            return False
        parts = [0] * k
        result = recursiveSearch(0, 0, 0)
        return result