class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1

        max_odd = 0
        min_even = float('inf')
        for val in count.values():
            if val % 2 == 1:
                max_odd = max(max_odd, val)
            else: 
                min_even = min(min_even, val)

        return max_odd - min_even
            