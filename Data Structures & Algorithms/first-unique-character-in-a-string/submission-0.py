class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int) 

        for letter in s:
            count[letter] += 1
        
        for i, letter in enumerate(s):
            if count[letter] == 1:
                return i

        return -1