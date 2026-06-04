class MyHashMap:

    def __init__(self):
        self.n = 10000
        self.hashMap = [False] * self.n
        

    def put(self, key: int, value: int) -> None:
        hashKey = key % self.n
        if self.hashMap[hashKey]: 
            if key in self.hashMap[hashKey][0]:
                key_loc = self.hashMap[hashKey][0].index(key)
                self.hashMap[hashKey][1][key_loc] = value
            else:
                self.hashMap[hashKey][0].append(key)
                self.hashMap[hashKey][1].append(value)
        else:
            self.hashMap[hashKey] = [[key],[value]]

    def get(self, key: int) -> int:
        hashKey = key % self.n
        if self.hashMap[hashKey]:
            if key in self.hashMap[hashKey][0]:
                idx = self.hashMap[hashKey][0].index(key)
                return self.hashMap[hashKey][1][idx]       
        return -1 


    def remove(self, key: int) -> None:
        hashKey = key % self.n
        self.hashMap[hashKey] = False


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)