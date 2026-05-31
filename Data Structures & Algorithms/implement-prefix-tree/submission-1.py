class PrefixTree:

    def __init__(self):
        self.prefix = dict()
        self.words = set()
        

    def insert(self, word: str) -> None:
        self.words.add(word)
        self.prefix.setdefault(word[0], {})
        insert = self.prefix[word[0]]
        for char in word[1:]:
            insert.setdefault(char, {})
            insert = insert[char]
        #print(self.prefix)
    
    def search(self, word: str) -> bool:
        return True if word in self.words else False
        

    def startsWith(self, prefix: str) -> bool:
        curSearch = self.prefix
        for char in prefix:
            if not char in curSearch:
                return False
            curSearch = curSearch[char]
        return True
