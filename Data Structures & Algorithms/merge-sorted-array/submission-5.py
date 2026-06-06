class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return        
        ptr1, ptr2, write = 0, 0, m
        while ptr1 < m and ptr2 < n:
            if nums1[ptr1] <= nums2[ptr2]:
                nums1[write] = nums1[ptr1]
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                nums1[write] = nums2[ptr2]
                ptr2 += 1
            write += 1
            if write == m + n:
                write = 0
        while ptr1 < m:
            nums1[write] = nums1[ptr1]
            ptr1 += 1
            write += 1
            if write == m + n:
                write = 0
        while ptr2 < n:
            nums1[write] = nums2[ptr2]
            ptr2 += 1
            write += 1
            if write == m + n:
                write = 0
        for i in range(n):
            nums2[i] = nums1[i+m]
        for i in range(m-1, -1, -1):
            nums1[i+n] = nums1[i]
        for i in range(n):
            nums1[i] = nums2[i]

            