class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        
        row_c = [0] * m
        col_c = [0] * n
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    row_c[row] += 1
                    col_c[col] += 1
        
        
        ans = []
        for row in range(m):
            ans.append([])
            for col in range(n):
                ans[row].append(2*row_c[row] - m + 2*col_c[col] - n)
        return ans