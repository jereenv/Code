class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        vis = {}

        def dfs(r,c):

            if r >= m:
                return 0
            
            if c >= n:
                return 0

            if r == m-1 and c == n-1:
                return 1

            if (r,c) in vis:
                return vis[(r,c)]


            vis[(r,c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return vis[(r,c)]
        
        return dfs(0,0)