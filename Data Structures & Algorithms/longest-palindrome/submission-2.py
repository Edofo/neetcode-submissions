class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        count = defaultdict(int)

        for x in s:
            count[x] += 1
        
        value = 0

        for x in count:
            if count[x] % 2 == 0:
                value += count[x]
            else:
                if value % 2 == 0:
                    value += 1
                value += count[x]-1

        return value