class Solution:
    def checkValidString(self, s: str) -> bool:
        stackP, stackS = [], []
        for i, char in enumerate(s):
            if char == "(":
                stackP.append(i)
            elif char == "*":
                stackS.append(i)
            else:
                if stackP:
                    stackP.pop()
                elif stackS:
                    stackS.pop()
                else:
                    print("EARLY END")
                    return False
        if len(stackP) > len(stackS):
            return False
        while stackP:
            idxP, idxS = stackP.pop(), stackS.pop()
            if idxP > idxS:
                return False
        return True
        