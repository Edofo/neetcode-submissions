class Solution:
    def isPalindrome(self, s: str) -> bool:
        il = 0
        ir = len(s)-1

        valid = "abcdefghijklmnopqrstuvwxyz0123456789"

        while il < ir:
            low_left = str(s[il]).lower()
            low_right = str(s[ir]).lower()
            if low_left not in valid:
                il += 1
                continue
            if low_right not in valid:
                ir -= 1
                continue
            if low_left != low_right:
                return False
            il+=1
            ir-=1

        return True