class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recArrGen(i, curRes, curSum):
            if i == len(nums):
                curSum += curRes
                print(curSum)
                return curSum
            a = recArrGen(i+1, curRes, curSum)
            b = recArrGen(i+1, curRes^nums[i], curSum)
            return a + b
        return recArrGen(0, 0, 0)