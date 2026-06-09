class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        count = {}
        mapping = {}

        for i in range(len(words)):
            count[i] = 0
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                count[i] = 1
            if i == 0:
                mapping[i] = count[i]
                continue
            mapping[i] = count[i] + mapping[i-1]
        
        tab = []
        for query in queries:
            if query[0] == 0:
                tab.append(mapping[query[1]])
                continue
            tab.append(mapping[query[1]] - mapping[query[0] - 1])
            
        return tab