class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bestSoFar = nums[0]
        maxProd = 1
        minProd = 1
        for num in nums:
            temp = max(minProd * num, maxProd * num, num)
            minProd = min(minProd * num, maxProd * num, num)
            maxProd = temp
            bestSoFar = max(bestSoFar, maxProd)
            print(num, minProd, maxProd, bestSoFar)
        return bestSoFar

        