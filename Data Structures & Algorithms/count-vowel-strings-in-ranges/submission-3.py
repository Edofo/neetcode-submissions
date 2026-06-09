class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set("aeiou")
        mapping = {}

        for i in range(len(words)):
            count = 0
            if words[i][0] in vowels and words[i][-1] in vowels:
                count = 1
            if i == 0:
                mapping[i] = count
                continue
            mapping[i] = count + mapping[i-1]
        
        tab = []
        for query in queries:
            if query[0] == 0:
                tab.append(mapping[query[1]])
                continue
            tab.append(mapping[query[1]] - mapping[query[0] - 1])
            
        return tab