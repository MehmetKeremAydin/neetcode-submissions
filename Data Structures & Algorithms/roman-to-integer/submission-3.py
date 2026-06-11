class Solution:
    def romanToInt(self, s: str) -> int:
        LUT = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        curVal = 0
        prevVal = math.inf
        totalVal = 0 
        for char in s:
            curVal = LUT[char]
            if curVal > prevVal:
                totalVal += curVal - 2*prevVal
            else:
                totalVal += curVal
            prevVal = curVal
        return totalVal