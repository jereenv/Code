class Solution:
    def countSubstrings(self, s: str) -> int:
        
        ans = [0]
        n = len(s)
        
        def countPalin(idx):
            ans[0] += 1
            l, r = idx - 1, idx + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                ans[0] += 1
                l -= 1
                r += 1
                
            l, r = idx, idx + 1
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    break
                ans[0] += 1
                l -= 1
                r += 1
                    
            
        
        for i in range(len(s)):
            countPalin(i)
        
        return ans[0]
        