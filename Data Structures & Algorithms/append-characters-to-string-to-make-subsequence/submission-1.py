class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        if len(t) == 0:
            return 0
        idxT = 0

        for letter in s:
            if t[idxT] == letter:
                idxT += 1
            if idxT == len(t):
                break;

        if idxT == len(t):
            return 0

        return len(t) - idxT
        