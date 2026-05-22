class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1Arr = [ord(char) - ord('0') for char in num1]
        n2Arr = [ord(char) - ord('0') for char in num2]
        total1 = 0
        total2 = 0
        for num in n1Arr:
            total1 *= 10
            total1 += num
        for num in n2Arr:
            total2 *= 10
            total2 += num
        print(total1, total2)
        mult = total1 * total2
        return str(mult)