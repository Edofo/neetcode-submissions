class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = defaultdict(int)

        for word in words:
            for char in word:
                count[char] += 1
        
        for c in count:
            print(count[c], count[c] % len(words))
            if count[c] % len(words) > 0:
                return False
        
        return True
        