class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        
        COL = len(grid[0])
        ROW = len(grid)
        
        @lru_cache(None)
        def dfs(r, c1, c2):
                
            if min(c1, c2) < 0 or max(c1, c2) >= COL or c1 == c2:
                return 0

            if r == ROW - 1:
                return grid[r][c1] + grid[r][c2]

            res = 0

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    res = max(res, dfs(r + 1, c1 + i, c2 + j))

            return grid[r][c1] + grid[r][c2] + res 
        
        return dfs(0, 0, COL - 1)