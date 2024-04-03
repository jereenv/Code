class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        
        ROW_MAX = len(board)
        COL_MAX = len(board[0])
        
        ans = [0]
        
        def dp(vis, curr, i, j):
            if curr == len(word):
                ans[0] = True
                return
            
            if i >= ROW_MAX or i < 0:
                return
            
            if j >= COL_MAX or j < 0:
                return
            
            if (i, j) in vis:
                return
            
            if word[curr] != board[i][j]:
                return
            
            vis.add((i, j))
            
            dp(vis, curr + 1, i + 1, j)
            dp(vis, curr + 1, i - 1, j)
            dp(vis, curr + 1, i, j - 1)
            dp(vis, curr + 1, i, j + 1)
            
            vis.remove((i, j))
            
        
        for r in range(ROW_MAX):
            for c in range(COL_MAX):
                if not ans[0]:
                    dp(set(), 0, r, c)
                else:
                    return ans[0]
        
        return ans[0]
                
        
            
            
        