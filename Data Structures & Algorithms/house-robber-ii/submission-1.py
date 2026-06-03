class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]
        def dfs(nums, hashID):
            if len(nums) in hashMap[hashID]:
                return hashMap[hashID][len(nums)]
            if not nums:
                return 0
            hashMap[hashID][len(nums)] = max(nums[0] + dfs(nums[2:], hashID), dfs(nums[1:], hashID))
            return hashMap[hashID][len(nums)]
        
        hashMap = [{}, {}]
        return max(dfs(nums[1:], 0), dfs(nums[:-1], 1))
    