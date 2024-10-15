class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        
        next_pos = 0
        
        for idx, val in enumerate(s):
            if val == "0":
                ans += idx - next_pos
                
                next_pos += 1
        
        return ans
        
            
        
        