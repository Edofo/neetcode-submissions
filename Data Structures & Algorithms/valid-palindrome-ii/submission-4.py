class Solution:
    def validPalindrome(self, s: str) -> bool:
        il = 0
        ir = len(s)-1
        count = 0

        while il < ir:
            if s[il] != s[ir]:
                skip_left = s[il+1:ir+1]
                skip_right = s[il:ir]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]
            il += 1
            ir -= 1
        
        return True
