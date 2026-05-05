class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = [0] * 101

        for height in heights:
            expected[height] += 1

        sort = []
        for i, val in enumerate(expected):
            if val > 0:
                for x in range(val):
                    sort.append(i)

        count = 0
        for i in range(len(heights)):
            if heights[i] != sort[i]:
                count += 1

        return count