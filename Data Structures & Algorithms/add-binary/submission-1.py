class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        result = ""
        if len(a) < len(b):
            a = (len(b)-len(a))*str(0) + a
        else:
            b = (len(a)-len(b))*str(0) + b
        carry = 0
        for i in range(len(b)-1, -1, -1):
            r = int(a[i]) + int(b[i]) + carry
            result = result + str(r%2)
            carry = (r - r%2) // 2
        result += str(carry)
        rev = result[::-1]
        return rev.lstrip("0")