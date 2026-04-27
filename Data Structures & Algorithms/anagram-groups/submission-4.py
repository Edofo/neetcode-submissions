class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tab = defaultdict(list)

        for text in strs:
            count = [0] * 26
            for char in text:
                count[ord(char) - ord("a")] += 1
            tab[tuple(count)].append(text)
        
        return list(tab.values())

