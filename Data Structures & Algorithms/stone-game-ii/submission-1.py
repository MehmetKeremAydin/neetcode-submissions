class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        def recursiveSearch(takenUntil, M, aliceTurn)-> tuple:
            if (takenUntil, M, aliceTurn) in memory: return memory[(takenUntil, M, aliceTurn)] 
            if takenUntil >= len(prefixSum):
                return 0, 0
            availableUntil = takenUntil + 2*M
            bobMax = 0
            aliceMax = 0
            for i in range(takenUntil+1, min(availableUntil+1, len(prefixSum))):
                nextM = max(i-takenUntil, M)
                aliceCount, bobCount = recursiveSearch(i, nextM, not aliceTurn)
                if aliceTurn and aliceCount + prefixSum[i]-prefixSum[takenUntil] > aliceMax:
                    aliceMax = aliceCount + prefixSum[i]-prefixSum[takenUntil]
                    bobMax = bobCount
                elif not aliceTurn and bobCount + prefixSum[i]-prefixSum[takenUntil] > bobMax:
                    bobMax = bobCount + prefixSum[i]-prefixSum[takenUntil]
                    aliceMax = aliceCount
            memory[(takenUntil, M, aliceTurn)] = (aliceMax, bobMax)
            return aliceMax, bobMax
        
        memory = {}
        prefixSum = [0]
        for i in range(len(piles)):
            prefixSum.append(prefixSum[i]+piles[i])
        aliceCount, _ = recursiveSearch(0, 1, True)
        return aliceCount