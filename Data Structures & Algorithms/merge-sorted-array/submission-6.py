class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ptr1, ptr2, write = m-1, n-1, m+n-1
        while ptr2 >= 0 and ptr1 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[write] = nums1[ptr1]
                ptr1 -= 1
            elif nums1[ptr1] <= nums2[ptr2]:
                nums1[write] = nums2[ptr2]
                ptr2 -= 1
            write -= 1
        while ptr2 >= 0:
            nums1[write] = nums2[ptr2]
            ptr2 -= 1
            write -= 1

            
        