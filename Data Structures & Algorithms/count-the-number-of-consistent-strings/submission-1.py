class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = len(words)
        check = set(allowed)
        for word in words:
            for letter in word:
                if letter not in check:
                    count -= 1
                    break

        return count