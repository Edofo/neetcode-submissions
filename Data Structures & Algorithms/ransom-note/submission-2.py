class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = [0] * 26

        for letter in magazine:
            count[ord(letter) - 97] += 1
        
        for letter in ransomNote:
            count[ord(letter) - 97] -= 1
            if count[ord(letter) - 97] < 0:
                return False

        return True