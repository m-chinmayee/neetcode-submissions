class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        id = hash(key) % self.size
        for pair in self.map[id]:
            if pair[0] == key:
                pair[1] = value
                return
        self.map[id].append([key, value])

    def get(self, key: int) -> int:
        id = hash(key) % self.size
        for pair in self.map[id]:
            if pair[0] == key:
                return pair[1]
        return -1
        
    def remove(self, key: int) -> None:
        id = hash(key) % self.size
        for i, pair in enumerate(self.map[id]):
            if pair[0] == key:
                del self.map[id][i]
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)