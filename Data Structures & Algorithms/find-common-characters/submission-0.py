class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        pool = Counter(words[0])
        for word in words[1:]:
            current = Counter(word)
            for letter in pool:
                pool[letter] = min(pool[letter], current[letter])
        result = []
        for letter in pool:
            for _ in range(pool[letter]):
                result.append(letter)
        return result