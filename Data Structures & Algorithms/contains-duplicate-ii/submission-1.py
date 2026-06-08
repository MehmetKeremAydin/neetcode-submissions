class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) < k+1:
            curWindow = set(nums) 
            return True if len(curWindow) < len(nums) else False
        else:
            left, right = 0, 0
            curWindow = set()
            while right < k+1:
                if nums[right] in curWindow:
                    return True
                curWindow.add(nums[right])
                right += 1
            while right < len(nums):
                curWindow.remove(nums[left])
                left+=1
                if nums[right] in curWindow:
                    return True
                curWindow.add(nums[right])
                right += 1
            return False
            
