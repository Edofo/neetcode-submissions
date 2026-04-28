class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        tab = set()

        for idx1, word in enumerate(words):
            for idx2, word2 in enumerate(words):
                if idx1 != idx2 and word in word2:
                    tab.add(word)
                    break;
        
        return list(tab)