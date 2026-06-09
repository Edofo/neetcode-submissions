class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        curr = 0
        new = ""

        for letter in s:
            if letter == "(":
                curr += 1
            if letter == ")":
                if curr > 0:
                    new += letter
                    curr -= 1
                continue
                
            new += letter

        result = ""
        for letter in reversed(new):
            if letter == "(" and curr > 0:
                curr -= 1
            else:
                result += letter
        return result[::-1]