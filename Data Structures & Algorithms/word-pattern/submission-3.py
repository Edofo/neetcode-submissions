class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        tab = [""] # split

        for letter in s:
            if letter == " ":
                tab.append("")
                continue
            tab[len(tab) - 1] += letter

        mapping1 = {}
        mapping2 = {}

        if len(tab) != len(pattern):
            return False

        for i in range(len(tab)):
            if pattern[i] in mapping1 and mapping1[pattern[i]] != tab[i]:
                return False
            if tab[i] in mapping2 and mapping2[tab[i]] != pattern[i]:
                return False
            mapping1[pattern[i]] = tab[i]
            mapping2[tab[i]] = pattern[i]

        return True