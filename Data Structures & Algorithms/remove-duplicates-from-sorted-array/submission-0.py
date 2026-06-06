class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 1, 1
        prev = nums[0]
        while read < len(nums):
            while read < len(nums) and nums[read] == prev :
                read += 1
            if read < len(nums):
                nums[write] = nums[read]
                prev = nums[write]
                write += 1
        return write
        