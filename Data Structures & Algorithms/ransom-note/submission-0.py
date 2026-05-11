class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = []
        for i in range(27):
            count.append(0)

        for letter in ransomNote:
            count[97-ord(letter)] += 1
        
        for letter in magazine:
            count[97-ord(letter)] -= 1

        for el in count:
            if el > 0:
                return False

        return True