class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        moved = 0
        start = -1
        while moved < len(nums):
            #print("start")
            start += 1
            nxt = (start + k) % len(nums)
            prev = nums[start]
            flag = True
            while flag:
                if nxt == start:
                    flag = False
                #print(nums)
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                nxt = (nxt + k) % len(nums)
                moved += 1

                