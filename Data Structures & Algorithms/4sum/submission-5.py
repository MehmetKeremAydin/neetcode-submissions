class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        nums = sorted(nums)
        print(nums)
        for i in range(len(nums)):
            if i>0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                curTarget = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                prevL, prevR = None, None
                print("I,J:", i, nums[i], j, nums[j], curTarget)
                while left < right:
                    curSum = nums[left] + nums[right]
                    print(left, nums[left], right, nums[right], curSum)
                    if curSum  == curTarget:
                        answer.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curTarget > curSum:
                        left += 1
                    else:
                        right -= 1

        return answer