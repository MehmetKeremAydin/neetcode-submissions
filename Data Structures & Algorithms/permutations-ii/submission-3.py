class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def recBT(curPerm, curHist):
            if len(curPerm) == len(nums):
                answer.append(curPerm)
                return
            keys = list(curHist.keys())
            for key in keys:
                curPerm.append(key)
                if curHist[key] == 1:
                    curHist.pop(key)
                else:
                    curHist[key] -= 1
                recBT(curPerm.copy(), curHist)
                curPerm.pop()
                curHist[key] = hist.get(key, 0) + 1
        
        hist = {}
        for n in nums:
            hist[n] = hist.get(n, 0) + 1
        
        answer = []
        curPerm = []
        recBT(curPerm, hist)
        return answer     