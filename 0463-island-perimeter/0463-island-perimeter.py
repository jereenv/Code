class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        ans = [0]
        
        vis = set()
        
        ROW = len(grid)
        COL = len(grid[0])
        
        def dfs(i, j):
            if (i, j) in vis:
                return
            
            if i < 0 or i >= ROW:
                ans[0] += 1
                return
            
            if j < 0 or j >= COL:
                ans[0] += 1
                return
            
            if grid[i][j] == 0:
                ans[0] += 1
                return
            
            vis.add((i, j))
            
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j - 1)
            dfs(i, j + 1)
            
            
        
        for i in range(0, ROW):
            for j in range(0, COL):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return ans[0]
        return ans[0]
            
            
        