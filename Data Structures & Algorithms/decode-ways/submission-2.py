class Solution:
    def numDecodings(self, s: str) -> int:
        def recursiveSearch(s:str)->int:
            if s in hashMap:
                return hashMap[s]
            if s == "":
                return 1
            if s[0] == "0":
                return 0
            sr1, sr2, sr3 = 0, 0, 0
            sr1 = recursiveSearch(s[1:])
            if len(s) >= 2:
                if s[0] == "1":
                    sr2 = recursiveSearch(s[2:])
                elif s[0] == "2" and s[1] in canFollowTwo:
                    sr3 = recursiveSearch(s[2:])
            hashMap[s] = sr1 + sr2 + sr3
            return hashMap[s]
        hashMap = {}
        canFollowTwo = set(["0", "1", "2", "3", "4", "5", "6"])
        return recursiveSearch(s)
        