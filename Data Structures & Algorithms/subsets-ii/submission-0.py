class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def recSearch(i:int, curSubset:list) -> None:
            if i == len(nums):
                answer.append(curSubset)
                return
            for j in range(numCnts[i]+1):
                if j>0:
                    curSubset.append(nums[i])
                recSearch(i+1, curSubset.copy())
            return

        
        answer = []
        subset = []
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        nums, numCnts = list(freq.keys()), list(freq.values())
        recSearch(0, subset)
        return answer
        



        