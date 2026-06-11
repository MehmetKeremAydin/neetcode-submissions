class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def bSearchLeft(start, end):
            l,r = start, end
            while l<=r:
                m = (l + r) // 2
                mV = known[m] if m in known else mountainArr.get(m)
                if mV == target:
                    return m
                elif mV < target:
                    l = m + 1
                else:
                    r = m - 1
            return l if mV == target else -1
        
        def bSearchRight(start, end):
            l,r = start, end
            while l<=r:
                m = (l + r) // 2
                mV = known[m] if m in known else mountainArr.get(m)
                if mV == target:
                    return m
                elif mV < target:
                    r = m - 1
                else:
                    l = m + 1
            return l if mV == target else -1


        known = {}
        l, r = 0, mountainArr.length() - 1
        while l <= r:
            midC = (l + r) // 2
            midL = midC - 1
            midR = midC + 1
            midCV = known[midC] if midC in known else mountainArr.get(midC)
            midLV = known[midL] if midL in known else mountainArr.get(midL)
            midRV = known[midR] if midR in known else mountainArr.get(midR)
            known[midC], known[midL], known[midR] = midCV, midLV, midRV
            if midLV < midCV < midRV:
                l = midC + 1
            elif midLV > midCV > midRV:
                r = midC - 1
            else:
                break
        assert midLV < midCV > midRV
        result = bSearchLeft(0, midC)
        if result != -1:
            return result
        result = bSearchRight(midC, mountainArr.length() - 1)
        return result