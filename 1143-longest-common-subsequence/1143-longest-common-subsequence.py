from functools import lru_cache
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        t1_MAX = len(text1)
        t2_MAX = len(text2)
        dp = {}
        
        def dfs(i, j):
            if i == t1_MAX or j == t2_MAX:
                return 0
                
            
            if (i, j) not in dp:
                if text1[i] == text2[j]:
                    dp[(i, j)] = 1 + dfs(i + 1, j + 1)
                else:
                    dp[(i, j)] = max(dfs(i+1, j), dfs(i, j + 1))
            return dp[(i, j)]
        
        return dfs(0, 0)