class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seqLUT = dict()
        max_len = 0
        for num in nums:
            if num in seqLUT:
                continue
            if num-1 in seqLUT and num+1 in seqLUT:
                seqLUT[num] = num
                entryL = seqLUT[num-1]
                entryR = seqLUT[num+1]
                seqLUT[entryL] = entryR
                seqLUT[entryR] = entryL
                max_len = max(max_len, entryR - entryL + 1)
            elif num-1 in seqLUT:
                entryL = seqLUT[num-1]
                seqLUT[num] = entryL
                seqLUT[entryL] = num
                max_len = max(max_len, num - entryL + 1)
            elif num+1 in seqLUT:
                entryR = seqLUT[num+1]
                seqLUT[num] = entryR
                seqLUT[entryR] = num
                max_len = max(max_len,  entryR - num + 1)
            else:
                seqLUT[num] = num
                max_len = max(1, max_len)
        return max_len
