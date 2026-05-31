class WordDictionary:

    def __init__(self):
        self.prefix = (dict(), False)
        

    def addWord(self, word: str) -> None:
        insertCur = self.prefix[0]
        for i,char in enumerate(word):
            insertCur.setdefault(char, [{}, False])
            if i == len(word) - 1:
                insertCur[char][1] = True 
            insertCur = insertCur[char][0]
            

    def search(self, word: str) -> bool:
        def recSearch(head:dict, word:str) -> bool:
            #print(head)
            if word == "":
                return head[1]
            if word[0] == ".":
                for child in head[0]:
                    found = recSearch(head[0][child], word[1:])
                    if found:
                        return True
                return False
            else:
                if word[0] in head[0]:
                    found = recSearch(head[0][word[0]], word[1:])
                    return found
                else:
                    return False
            
        found = recSearch(self.prefix, word)
        return found
        
