class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        def recursiveGame(takenUntil:int, aliceTurn:bool) -> tuple(int, int):
            if (takenUntil, aliceTurn) in memory: return memory[(takenUntil, aliceTurn)]
            if takenUntil >= len(stoneValue):
                return 0, 0
            aliceMax, bobMax = -math.inf, -math.inf
            turnTotal = 0
            for i in range(2,-1,-1):
                if takenUntil + i >= len(stoneValue): continue
                turnTotal = sum([stoneValue[takenUntil + j] for j in range(i+1)])
                aliceScore, bobScore = recursiveGame(takenUntil+i+1, not aliceTurn)
                if aliceTurn and aliceScore + turnTotal > aliceMax:
                    aliceMax = aliceScore + turnTotal
                    bobMax = bobScore
                if not aliceTurn and bobScore + turnTotal > bobMax:
                    bobMax = bobScore + turnTotal
                    aliceMax = aliceScore
            memory[(takenUntil, aliceTurn)] = (aliceMax, bobMax)
            return aliceMax, bobMax

        memory = {}
        aliceScore, bobScore = recursiveGame(0, True)
        if aliceScore == bobScore: return "Tie"
        return "Alice" if aliceScore > bobScore else "Bob"