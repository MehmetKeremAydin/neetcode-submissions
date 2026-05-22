class CountSquares:

    def __init__(self):
        self.LUT = dict()      

    def add(self, point: List[int]) -> None:
        x, y = point
        if x in self.LUT:
            self.LUT[x][y] = self.LUT[x].get(y, 0) + 1
        else:
            self.LUT[x] = {y: 1}
        #print(self.LUT)


    def count(self, point: List[int]) -> int:
        #print("*******COUNT LOGIC********")
        #print(point)
        xPiv, yPiv = point
        if not (xPiv in self.LUT):
            return 0
        squareCount = 0
        for yCrd in self.LUT[xPiv]:
            edgeLen = abs(yCrd - yPiv)
            if edgeLen == 0:
                continue
            if ((xPiv+edgeLen in self.LUT) and 
            (yPiv in self.LUT[xPiv+edgeLen]) and 
            (yCrd in self.LUT[xPiv+edgeLen])):
                cnt1 = self.LUT[xPiv][yCrd]
                cnt2 = self.LUT[xPiv+edgeLen][yCrd]
                cnt3 = self.LUT[xPiv+edgeLen][yPiv]
                print(cnt1, cnt2, cnt3)
                squareCount += cnt1 * cnt2 * cnt3
            if((xPiv-edgeLen in self.LUT) and 
            (yPiv in self.LUT[xPiv-edgeLen]) and 
            (yCrd in self.LUT[xPiv-edgeLen])):
                cnt1 = self.LUT[xPiv][yCrd]
                cnt2 = self.LUT[xPiv-edgeLen][yPiv]
                cnt3 = self.LUT[xPiv-edgeLen][yCrd]
                print(cnt1, cnt2, cnt3)
                squareCount += cnt1 * cnt2 * cnt3
            #print(yCrd, edgeLen, squareCount)
        #print("*******END OF COUNT LOGIC********")
        return squareCount
