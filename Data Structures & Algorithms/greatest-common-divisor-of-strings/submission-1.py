class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        limit = min(len(str1), len(str2))
        answer = ""
        for i in range(1, limit+1):
            if len(str1) % i == 0 and len(str2) % i == 0:
                coef1, coef2 = len(str1) // i, len(str2) // i
            else:
                continue
            substr = str1[:i]
            if str1 == coef1 * substr and str2 == coef2 * substr:
                answer = substr
        return answer