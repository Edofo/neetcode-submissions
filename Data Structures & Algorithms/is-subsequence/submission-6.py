class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        idxS = 0

        for letter in t:
            if s[idxS] == letter:
                idxS += 1
            if idxS == len(s):
                return True

        return False
        
        

        