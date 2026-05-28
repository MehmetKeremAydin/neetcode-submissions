class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(s: str) -> bool:
            if s == None or s == "":
                return False
            lPtr, rPtr = 0, len(s) - 1
            while rPtr > lPtr:
                if s[lPtr] != s[rPtr]:
                    return False
                lPtr += 1
                rPtr -= 1
            return True
        
        def recursivePartition(rem_chars:str, parts:list) -> None:
            #print(rem_chars, parts)
            if rem_chars == "" or rem_chars == None:
                answer.append(parts)
                return
            if isPalindrome(rem_chars):
                parts.append(rem_chars)
                answer.append(parts.copy())
                parts.pop()
            for i in range(0, len(rem_chars)):
                part1 = rem_chars[:i]
                part2 = rem_chars[i:]
                #print(part1, part2)
                if isPalindrome(part1):
                    parts.append(part1)
                    recursivePartition(part2, parts)
                    parts.pop()
            return
        
        answer = list()
        cur_prttn = list()
        recursivePartition(s, cur_prttn)
        return answer
        



        