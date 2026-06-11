class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def recArrGen(i, curArr):
            if i == len(nums):
                if curArr:
                    result = curArr[0]
                    for i in range(1, len(curArr)):
                        result ^= curArr[i]
                    return result
                else:
                    return 0
            sum1 = recArrGen(i+1, curArr.copy())
            curArr.append(nums[i])
            sum2 = recArrGen(i+1, curArr.copy())
            return sum1 + sum2


        arr = []
        return recArrGen(0, arr)