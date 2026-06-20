class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        rangeLUT = {}
        maxLen = 0
        for i in nums:
            if i in rangeLUT:
                continue
            rangeLUT[i] = [0,0]
            if i-1 in rangeLUT:
                rangeLUT[i][0] = rangeLUT[i-1][0] + 1
            if i+1 in rangeLUT:
                rangeLUT[i][1] = rangeLUT[i+1][1] + 1
            curLen = rangeLUT[i][0] + rangeLUT[i][1] + 1
            if rangeLUT[i][0] != 0:
                rangeLUT[i-rangeLUT[i][0]][1] = curLen - 1
            if rangeLUT[i][1] != 0:
                rangeLUT[i+rangeLUT[i][1]][0] = curLen - 1
            maxLen = max(maxLen, curLen)
        return maxLen    