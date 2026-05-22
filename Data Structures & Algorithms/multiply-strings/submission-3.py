class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1Arr = [ord(char) - ord('0') for char in num1]
        n2Arr = [ord(char) - ord('0') for char in num2]
        result = [0] * (len(num1) + len(num2))
        for i, n1 in enumerate(reversed(n1Arr)):
            overflow = 0
            for j, n2 in enumerate(reversed(n2Arr)):
                mult = n1 * n2 + overflow
                overflow = mult // 10
                result[i+j] += mult % 10
            result[i+j+1] += overflow
        total = 0
        for num in reversed(result):
            total *= 10
            total += num
        return str(total)