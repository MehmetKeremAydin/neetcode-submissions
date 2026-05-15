class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        nSum = n1 + n2
        p1 = n1//2
        p2 = nSum // 2 - p1
        parted = False
        while(not parted):
            pl1 = nums1[p1-1] if p1 != 0 else -math.inf
            pl2 = nums2[p2-1] if p2 != 0 else -math.inf
            pr1 = nums1[p1] if p1 != n1 else math.inf
            pr2 = nums2[p2] if p2 != n2 else math.inf
            if(pl1 <= pr2 and pl2 <= pr1):
                parted = True
            elif pr2 <= pl1: # This is still O(min(m,n)), Wtf is this question? Make search for partition binary to solve in log.
                p1 -= 1
                p2 += 1
            elif pr1 <= pl2:
                p1 += 1
                p2 -= 1
        if nSum % 2 == 0:
            return (max(pl1, pl2)+ min(pr1, pr2)) / 2
        else:
            return min(pr1, pr2)