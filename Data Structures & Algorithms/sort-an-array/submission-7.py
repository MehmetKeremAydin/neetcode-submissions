class Solution: # 1 3 4 2 5 6
    def sortArray(self, nums: List[int]) -> List[int]:
        def recQSort(num, start, end):
            if start == end:
                return
            elif end - start == 1:
                if num[start] > num[end]:
                    num[start], num[end] = num[end], num[start]
                return
            pivot = sorted([num[start], num[(start+end+1)//2], num[end]])[0]
            left, right = start, end 
            cursor = start
            last_center = start
            applied_change = False
            while left <= right:
                if num[left] <= pivot:
                    if num[left] == pivot:
                        pivot_loc = left
                    left += 1
                else:
                    num[left], num[right] = num[right], num[left]
                    applied_change = True
                    right -= 1
            if not applied_change:
                return
            #num[right], num[pivot_loc] = num[pivot_loc], num[right]
            #print(nums, pivot, start, end, left, right)
            recQSort(num, start, right)
            recQSort(num, left, end)
                
        recQSort(nums, 0, len(nums)-1)
        return nums


        
        
        