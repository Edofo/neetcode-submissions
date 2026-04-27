class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tab = {}

        for text in strs:
            count = [0] * 26
            for char in text:
                count[ord(char) - ord("a")] += 1
            key = tuple(count)
            if key not in tab:
                tab[key] = []
            tab[key].append(text)
        
        return list(tab.values())

