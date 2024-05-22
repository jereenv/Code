class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res= []
        part = []
        
        n = len(s)
        
        def dfs(idx):
            if idx >= n:
                res.append(part.copy())
            
            for j in range(idx, n):
                if self.isPali(s, idx, j):
                    part.append(s[idx: j + 1])
                    dfs(j + 1)
                    part.pop()
                    
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
    
        