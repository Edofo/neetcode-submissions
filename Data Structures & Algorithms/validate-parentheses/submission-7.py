class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {")": "(", "]": "[", "}": "{"}

        for letter in s:
            if letter in match:
                if not stack or stack.pop() != match[letter]:
                    return False
            else:
                stack.append(letter)

        return len(stack) == 0