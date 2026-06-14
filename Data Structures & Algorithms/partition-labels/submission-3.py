class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppLUT = {}
        res = []
        for i,char in enumerate(s):
            lastAppLUT[char] = i
        print(lastAppLUT)
        begin = end = - 1
        while end < len(s) - 1:
            begin = cur = end + 1
            end = lastAppLUT[s[begin]]
            while cur < end and end < len(s) - 1:
                end = max(end, lastAppLUT[s[cur]])
                cur += 1
            res.append(end-begin+1)
        return res





        