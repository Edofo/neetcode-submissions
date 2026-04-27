class Solution:
    def minOperations(self, s: str) -> int:
        change1 = 0 # 101...
        change2 = 0 # 010...

        for i, char in enumerate(s):
            if i % 2 == 0:
                if char == "1":
                    change2 += 1
                else:
                    change1 += 1
            else:
                if char == "0":
                    change2 += 1
                else:
                    change1 += 1

        return min(change1, change2)
        