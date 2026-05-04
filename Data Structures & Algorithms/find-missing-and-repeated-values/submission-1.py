class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        missing = set()

        for i in range(1, len(grid) * len(grid[0]) + 1):
            missing.add(i)
        
        repeat = None

        for row in grid:
            for el in row:
                if el in missing:
                    missing.remove(el)
                    continue
                if el not in missing:
                    repeat = el

        return [repeat, missing.pop()]

        