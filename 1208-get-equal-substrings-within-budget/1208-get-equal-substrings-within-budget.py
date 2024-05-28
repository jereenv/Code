class Solution:
    
    def getCost(self, a, b):
        return abs(ord(a) - ord(b))
    
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
        ans = 0
        l, r = 0, 0
        n = len(s)
        total = 0
        
        while r < n:
            curr = self.getCost(s[r], t[r])
            total += curr
            
            while total > maxCost:
                total -= self.getCost(s[l], t[l])
                l += 1
            
            ans = max(ans, r - l + 1)
            r += 1
        
        return ans
        
        
    
    
    
        