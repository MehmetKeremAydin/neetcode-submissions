class Solution:
    def minEnd(self, n: int, x: int) -> int:
        i = 0
        x_bits = set()
        while x > 0:
            if x % 2 == 1:
                x_bits.add(i)
            x //= 2
            i += 1
        result = 0
        i = 0
        n = n - 1
        while n > 0:
            if i in x_bits:
                x_bits.remove(i)
                result += 1 << i
            else:
                rem = n % 2
                n //= 2
                if rem == 1:
                    result += 1 << i
            i += 1
        while x_bits:
            b = x_bits.pop()
            result += 1 << b
        return result
        