class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def testRecursive(i, target, subset):
            if target == 0:
                answer.append(subset)
                return
            elif target < 0 or i==len(frequency):
                return
            for j in range(counts[i]+1):
                if j>0:
                    subset.append(nums[i])
                #print(i, j, target-j*nums[i], subset)
                testRecursive(i+1, target-j*nums[i], subset.copy())
            return

        
        answer = []
        subset = []
        frequency = dict()
        for num in candidates:
            frequency[num] = frequency.get(num, 0) + 1
        nums, counts = list(frequency.keys()), list(frequency.values())
        testRecursive(0, target, subset)
        return answer