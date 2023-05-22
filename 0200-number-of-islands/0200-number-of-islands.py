class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        maxRow = len(grid)
        maxCol = len(grid[0])

        def dfs(r, c):
            if r >= maxRow or r < 0:
                return 0
            if c >= maxCol or c < 0:
                return 0
            
            if grid[r][c] != "1":
                return 0
            
            grid[r][c] = 0
            return 1 + dfs(r-1,c) + dfs(r + 1, c) + dfs (r, c-1) + dfs(r, c+ 1)
        
        islands = 0
        for row in range(maxRow):
            for col in range(maxCol):
                if dfs(row, col) > 0:
                    islands += 1
        
        return islands