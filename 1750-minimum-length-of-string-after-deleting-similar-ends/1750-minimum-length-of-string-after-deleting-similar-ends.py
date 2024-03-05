class Solution:
    def minimumLength(self, s: str) -> int:
        ans = len(s)
        
        l, r = 0, ans - 1
        
        while l < r:
            curr = s[l]
            
            if s[r] != curr:
                break
            
            while s[r] == curr and l < r:
                r -= 1
                ans -= 1
            
            while s[l] == curr and l <= r:
                l += 1
                ans -= 1
        return ans
                
        