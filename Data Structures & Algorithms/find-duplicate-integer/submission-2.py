class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if (i+1 == n):
                continue
            elif n < i + 1 or nums[n-1] == n:
                return n
            hold = nums[n-1]
            while(hold!=n):
                next_hold = nums[hold-1]
                if(hold == nums[hold-1]):
                    return hold
                nums[hold-1] = hold
                hold = next_hold
            nums[n-1] = n
        return 0

            
        