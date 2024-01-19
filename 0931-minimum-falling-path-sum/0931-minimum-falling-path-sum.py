class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
    
        ROW_MAX = len(matrix)
        COL_MAX = len(matrix[0])
        
        memo = {}
        
        def dp(r, c):
            
            if r == -1:
                return 0
            
            if c == COL_MAX or c < 0:
                return 10000
            
            if (r, c) not in memo:
                memo[(r, c)] = matrix[r][c] + min(dp(r - 1, c - 1), dp(r-1, c), dp(r-1, c + 1))
            return memo[(r, c)]
        
        return min(dp(ROW_MAX-1, i) for i in range(COL_MAX))