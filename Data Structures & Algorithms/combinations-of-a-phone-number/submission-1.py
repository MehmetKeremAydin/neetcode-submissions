class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        LUT = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        
        def recursiveGen(remDigits, curComb):
            if remDigits == "":
                answer.append(curComb)
                return
            for letter in LUT[remDigits[0]]:
                curComb += letter
                recursiveGen(remDigits[1:], curComb)
                curComb = curComb[:-1]

        if digits == "":
            return []
        answer = []
        combination = ""
        recursiveGen(digits, combination)
        return answer
