class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        value = -1
        for i in range(len(s)):
            if s[i] in first:
                value = max(value, i - first[s[i]] - 1)
            else:
                first[s[i]] = i
        return value