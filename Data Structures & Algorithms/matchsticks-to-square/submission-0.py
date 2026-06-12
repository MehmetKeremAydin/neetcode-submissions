class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        def recursiveSearch(i, curParts):
            #print(i, curParts)
            if i == len(matchsticks):
                if all(x == sideLen for x in curParts):
                    return True
                else:
                    return False
            if not all(x <= sideLen for x in curParts):
                return False
            for j in range(4):
                curParts[j] += matchsticks[i] 
                result = recursiveSearch(i+1, curParts)
                if result:
                    return True
                curParts[j] -= matchsticks[i]
            return False
                   
        maxLen = 0
        perimeter = 0
        for stick in matchsticks:
            perimeter += stick
            maxLen = max(maxLen, stick)
        sideLen = perimeter // 4
        if sideLen * 4 != perimeter or maxLen > sideLen:
            #print("EXIT EARLY")
            return False
        partition = [0,0,0,0]
        result = recursiveSearch(0, partition)
        return result

        