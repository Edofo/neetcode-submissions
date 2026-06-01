class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for letter in s:
            if letter == ")" or letter == "}" or letter == "]":
                if len(stack) == 0:
                    return False
                if letter == ")" and stack.pop() != "(":
                    return False
                if letter == "]" and stack.pop() != "[":
                    return False
                if letter == "}" and stack.pop() != "{":
                    return False
            else:
                stack.append(letter)

        return len(stack) == 0