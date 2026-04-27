class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        idx = 0

        while idx < len(s) - 1:
            total += abs(ord(s[idx]) - ord(s[idx + 1]))
            idx += 1
        
        return total