class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recArrGen(i, curRes):
            if i == len(nums):
                return curRes
            a = recArrGen(i+1, curRes)
            b = recArrGen(i+1, curRes^nums[i])
            return a + b
        return recArrGen(0, 0)