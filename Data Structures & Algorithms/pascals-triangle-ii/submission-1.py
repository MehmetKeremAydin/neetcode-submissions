class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]
        prev = [1, 1]
        for i in range(rowIndex-1):
            cur = []
            for j in range(1,len(prev)):
                cur.append(prev[j-1] + prev[j])
            prev = [1] + cur + [1]
        return prev
        