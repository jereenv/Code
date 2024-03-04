class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colSet = set()
        rowSet = set()
        
        ROW = len(matrix)
        COL = len(matrix[0])
        
        for row in range(ROW):
            for col in range(COL):
                if matrix[row][col] == 0:
                    colSet.add(col)
                    rowSet.add(row)
        
        def makeColZero(col):
            for row in range(ROW):
                matrix[row][col] = 0
        
        def makeRowZero(row):
            for col in range(COL):
                matrix[row][col] = 0
        
        for row in range(ROW):
            for col in range(COL):
                if col in colSet or row in rowSet:
                    matrix[row][col] = 0

        