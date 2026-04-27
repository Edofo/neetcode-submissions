class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        for i in range(len(s) - 1, -1, -1):
            letter = s[i]
            if letter != " ":
                count += 1
            if letter == " " and count > 0:
                return count
        
        return count
        