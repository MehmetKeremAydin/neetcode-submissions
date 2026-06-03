class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min([len(i) for i in strs])
        answer = ""
        for i in range(minLen):
            testChar = strs[0][i]
            for j in range(1, len(strs)):
                if testChar != strs[j][i]:
                    return answer
            answer = answer + testChar
        return answer