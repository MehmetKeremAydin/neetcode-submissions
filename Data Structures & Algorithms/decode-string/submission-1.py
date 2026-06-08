class Solution:
    def findCloser(self, s, start):
        count = 0
        for i in range(start, len(s)):
            if s[i] == '[':
                count += 1
            elif s[i] == ']':
                if count == 1:
                    return i
                else:
                    count -= 1
                  
    def decodeString(self, s: str) -> str:
        answer = ""
        i = 0
        while i < len(s):
            char = s[i]
            if char.isalpha():
                answer += char
            elif char.isdigit():
                idx = s.find("[", i)
                mult = int(s[i:idx])
                end = self.findCloser(s, idx)
                substr = self.decodeString(s[idx+1:end])
                answer += mult*substr
                i = end
            i += 1
        return answer

            