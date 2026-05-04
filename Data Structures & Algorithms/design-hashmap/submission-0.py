class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.tab = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        idx = key % self.size
        for i, (k, v) in enumerate(self.tab[idx]):
            if k == key:
                self.tab[idx][i] = (key, value)
                return
        self.tab[idx].append((key, value))

    def get(self, key: int) -> int:
        idx = key % self.size
        for k, v in self.tab[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = key % self.size
        for i, (k, v) in enumerate(self.tab[idx]):
            if k == key:
                self.tab[idx].pop(i)
                return