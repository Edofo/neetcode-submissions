class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tab = []
        map = {}

        for text in strs:
            total = ""
            textTamp = "".join(sorted(text))

            if textTamp not in map:
                map[textTamp] = len(tab)
                tab.append([])

            tab[map[textTamp]].append(text)
            print(total)
        
        return tab

