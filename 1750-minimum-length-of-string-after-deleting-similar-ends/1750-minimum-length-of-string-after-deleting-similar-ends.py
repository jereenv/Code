class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        
        while l < r:
            curr = s[l]
            
            if s[r] != curr:
                break
            
            while s[r] == curr and l < r:
                r -= 1
            
            while s[l] == curr and l <= r:
                l += 1
        return r - l + 1
                
        