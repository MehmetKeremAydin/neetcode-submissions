class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queueR, queueD = deque(), deque()
        for i, char in enumerate(senate):
            if char == "R":
                queueR.append(i)
            elif char == "D":
                queueD.append(i)
        while queueR and queueD:
            R, D = queueR.popleft(), queueD.popleft()
            if R < D:
                queueR.append(R + len(senate))
            else:
                queueD.append(D + len(senate))
        return "Radiant" if queueR else "Dire"