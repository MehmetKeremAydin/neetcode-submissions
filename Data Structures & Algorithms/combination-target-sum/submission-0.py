class Solution:    
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def dfs(i:int, target, subset:list) -> None:
            if target == 0:
                answer.append(subset)
                return
            if target < 0 or i==len(nums):
                return
            for j in range(trialCounts[i]+1):
                if j>0:
                    subset.append(nums[i])
                #print(i, j, target-j*nums[i], subset, answer)
                dfs(i+1, target-j*nums[i], subset.copy())

        answer = []
        sub = []
        trialCounts = [target // num for num in nums]
        dfs(0, target, sub)
        
        return  answer
        