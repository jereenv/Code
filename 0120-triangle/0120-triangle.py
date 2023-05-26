class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        vis = {}
        def dfs(row, ind):
            if row == 0:
                if ind != 0:
                    return float('inf')
                else:
                    return triangle[row][ind]
            if ind >= len(triangle[row]) or row >= len(triangle) or ind < 0 or row < 0:
                return float('inf')
            
            if (row, ind) not in vis:
                vis[(row,ind)] = triangle[row][ind] + min(dfs(row-1, ind), dfs(row-1, ind - 1))
            return vis[(row,ind)]
        
        
        m = float('inf')
        n = len(triangle) - 1
        for i in range(len(triangle[n])):
            m = min(m, dfs(n, i))
        return m
            