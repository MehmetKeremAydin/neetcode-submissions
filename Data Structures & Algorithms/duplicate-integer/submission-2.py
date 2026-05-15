class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memory = set()
        for num in nums:
            if num in memory:
                return True
            memory.add(num)
        return False
        