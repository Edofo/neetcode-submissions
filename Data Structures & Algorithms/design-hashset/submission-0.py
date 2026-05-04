class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.set = [[] for _ in range(self.size)]

    def add(self, key: int) -> None:
        idx = key % self.size
        if key not in self.set[idx]:
            self.set[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % self.size
        if key in self.set[idx]:
            self.set[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % self.size
        return key in self.set[idx]