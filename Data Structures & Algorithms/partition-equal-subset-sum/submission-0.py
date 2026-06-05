class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        cumSum = set([0])
        target = sum(nums)
        if target % 2 == 1:
            return False
        target = target // 2
        for num in nums:
            newSet = set()
            for curSum in cumSum:
                newSet.add(curSum + num)
            cumSum = cumSum.union(newSet)
            if target in cumSum:
                return True
        return False
                