class Solution:
    def customSortString(self, order: str, s: str) -> str:
        idxs = {}

        for i in range(len(order)):
            idxs[order[i]] = i

        return "".join(sorted(s, key=lambda x: idxs.get(x, 26)))