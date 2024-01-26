class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        
        ans = [0]
        
        vis = {}
        def dfs(i, j, p):
            if (i == m or i < 0 or j == n or j < 0):
                
                return 1
            
            if p == maxMove:
                return 0
            
            
            p += 1
            
            if (i, j, p) not in vis:
                vis[(i, j, p)] = dfs(i + 1, j, p) + dfs(i, j + 1, p) + dfs(i - 1, j, p) + dfs(i, j - 1, p)
            
            return vis[(i, j, p)]
            
            
       
        return dfs(startRow, startColumn, 0) % (10**9 + 7)