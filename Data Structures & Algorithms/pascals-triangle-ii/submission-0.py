class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tab = [[1]]

        for row in range(1, rowIndex + 1):
            tab.append([])
            for col in range(row + 1):
                if col == 0 or col == row:
                    tab[row].append(1)
                    continue
                tab[row].append(tab[row-1][col-1] + tab[row-1][col])

        return tab[len(tab) - 1]