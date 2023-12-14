class Solution:
    def findLonelyPixel(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        row_count = [0] * m
        col_count = [0] * n
        
        for row in range(m):
            for col in range(n):
                if mat[row][col] == "B":
                    row_count[row] += 1
                    col_count[col] += 1
        
        ans = 0
        for row in range(m):
            for col in range(n):
                if mat[row][col] == "B":
                    if row_count[row] == 1 and col_count[col] == 1:
                        ans += 1

        return ans