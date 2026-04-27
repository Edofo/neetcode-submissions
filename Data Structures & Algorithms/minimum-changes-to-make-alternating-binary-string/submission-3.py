class Solution:
    def minOperations(self, s: str) -> int:
        change1 = 0 # 101...
        for i, char in enumerate(s):
            if i % 2 == 0:
                if char == "1":
                    change1 += 1
            else:
                if char == "0":
                    change1 += 1

        return min(change1, len(s) - change1)
        