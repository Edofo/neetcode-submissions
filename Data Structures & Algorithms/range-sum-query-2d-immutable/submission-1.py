class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = []
        for row in range(len(matrix)):
            self.matrix.append([])
            for col in range(len(matrix[row])):
                count = matrix[row][col]
                if row > 0:
                    count += self.matrix[row-1][col]
                if col > 0:
                    count += self.matrix[row][col-1]
                if row > 0 and col > 0:
                    count -= self.matrix[row-1][col-1]
                self.matrix[row].append(count)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        count = self.matrix[row2][col2]
        if row1 > 0:
            count -= self.matrix[row1-1][col2]
        if col1 > 0:
            count -= self.matrix[row2][col1-1]
        if row1 > 0 and col1 > 0:
            count += self.matrix[row1-1][col1-1]
        return count