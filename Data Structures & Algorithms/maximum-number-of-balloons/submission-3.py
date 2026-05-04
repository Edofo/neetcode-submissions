class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = {
            "b": 0,
            "a": 0,
            "l": 0,
            "o": 0,
            "n": 0
        }

        for letter in text:
            if letter in word:
                word[letter] += 1

        return min(word["b"], word["a"], word["l"] // 2, word["o"] // 2, word["n"])