class MyHashSet:

    def __init__(self):
        self.n = 10000
        self.data = [False] * self.n
        

    def add(self, key: int) -> None:
        hashedKey = key % self.n
        if self.data[hashedKey] == False:
            self.data[hashedKey] = [key]
        else:
            self.data[hashedKey].append(key)

    def remove(self, key: int) -> None:
        hashedKey = key % self.n
        self.data[hashedKey] = False
        

    def contains(self, key: int) -> bool:
        hashedKey = key % self.n
        return True if self.data[hashedKey] != False else False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)