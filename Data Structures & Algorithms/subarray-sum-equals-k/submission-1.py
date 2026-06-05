class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = [0] * (len(nums) + 1)
        for i,num in enumerate(nums):
            total[i+1] = total[i] + num
        hMap = dict()
        counter = 0
        for t in total:
            if t-k in hMap:
                counter += hMap[t-k]
            hMap[t] = hMap.get(t, 0) + 1
        return counter
            

