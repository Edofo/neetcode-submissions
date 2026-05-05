class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mapping = defaultdict(int)
        for el in arr:
            mapping[el] += 1

        highest = -1
        for el in mapping:
            if el == mapping[el] and el > highest:
                highest = el

        return highest
