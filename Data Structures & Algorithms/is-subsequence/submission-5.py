class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        idxS = 0

        for letter in t:
            print(s[idxS], letter, idxS)
            if s[idxS] == letter:
                idxS += 1
            print(idxS)
            if idxS == len(s):
                return True

        return False
        
        

        