class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter = {}

        for letter in s:
            if counter.get(letter):
                counter[letter] = counter[letter] + 1
            else:
                counter[letter] = 1
                    
        for letter in t:
            if counter.get(letter):
                counter[letter] = counter[letter] - 1
            else:
                return False
        
        return True
        