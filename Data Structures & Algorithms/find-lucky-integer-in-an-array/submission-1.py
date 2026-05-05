class Solution:
    def findLucky(self, arr: List[int]) -> int:
        mapping = {}
        for el in arr:
            if el in mapping:
                mapping[el] += 1
            else:
                mapping[el] = 1

        highest = -1
        for el in mapping:
            if el == mapping[el]:
                if el > highest:
                    highest = el

        return highest
