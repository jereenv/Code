class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        maxR = len(grid)
        maxC = len(grid[0])
        
        def dfs(r,c):
            if r >= 0 and r < maxR and c >= 0 and c < maxC and grid[r][c] == 1:
                grid[r][c] = 0
                return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
            return 0
        maxA = 0
        for i in range(maxR):
            for j in range(maxC):
                maxA = max(maxA, dfs(i,j))
        
        return maxA