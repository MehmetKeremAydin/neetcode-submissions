class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + 1
            if digits[i] < 10:
                break
            digits[i] = 0
            if i == 0:
                digits.insert(0,1)
                break
        return digits