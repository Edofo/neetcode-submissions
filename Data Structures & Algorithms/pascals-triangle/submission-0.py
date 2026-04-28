class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tab = [[1]]

        for row in range(1, numRows):
            tab.append([])
            for col in range(row + 1):
                if col == 0 or col == row:
                    tab[row].append(1)
                else:
                    valLeft = 0
                    valRight = 0
                    tab[row].append(tab[row-1][col-1] + tab[row-1][col])

        return tab