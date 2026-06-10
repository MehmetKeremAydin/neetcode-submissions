class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            rem = (columnNumber-1)  % 26
            ans += chr(ord("A")+rem)
            columnNumber = (columnNumber-1) // 26
        return ans[::-1]