class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        tab = []
        map = {}

        for text in strs:
            total = ""
            textTamp = sorted(text)
            for letter in textTamp:
                total = total + str(ord(letter))
            if total not in map:
                map[total] = len(tab)
                tab.append([])

            tab[map[total]].append(text)
            print(total)
        
        return tab

