class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colRow = set()
        
        ROW = len(matrix)
        COL = len(matrix[0])
        
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col] == 0:
                    colRow.add((row, col))
        
        def makeColZero(col):
            print(col)
            for row in range(ROW):
                matrix[row][col] = 0
        
        def makeRowZero(row):
            for col in range(COL):
                matrix[row][col] = 0
        
        for row, col in colRow:
            makeColZero(col)
            makeRowZero(row)
        
        print(matrix)