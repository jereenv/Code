class Solution:
    def compress(self, chars: List[str]) -> int:
        
        ans = []
        
        
        prev = chars[0]
        ct = 1
        
        k = 0
        
        for idx, char in enumerate(chars):
            if idx == 0:
                continue
            
            if char != prev:
                chars[k] = prev
                k += 1
            
                if ct > 1:
                    for i in str(ct):
                        chars[k] = i
                        k += 1
                prev = char
                ct = 1
            else:
                ct += 1
        chars[k] = prev
        k += 1
        if ct > 1:
            for i in str(ct):
                chars[k] = i
                k += 1
        
        return k
                
                    
            
            
        