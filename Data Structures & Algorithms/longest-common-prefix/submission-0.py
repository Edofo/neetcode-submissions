class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs[1:]:
            for i in range(min(len(prefix), len(word))):
                letter = word[i]
                if letter != prefix[i]:
                    prefix = prefix[:i]
                    break;
            prefix = prefix[:len(word)]
        
        return prefix
        