class Solution:

    def encode(self, strs: List[str]) -> str:
        message = str()
        for word in strs:
            length = str(len(word))
            message += length + '#' + word
        return message


    def decode(self, s: str) -> List[str]:
        message = list()
        i = 0
        print(s)
        while(i != len(s)):
            hash_idx = s.find('#', i, len(s))
            length = int(s[i:hash_idx])
            word = s[(hash_idx+1):(hash_idx+1+length)]
            message.append(word)
            i = hash_idx + length + 1
        return message