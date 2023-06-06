class Solution:
    def trap(self, h: List[int]) -> int:
        
        result = 0
        l = 0
        r = len(h) - 1
        
        l_max = 0
        r_max = 0
        
        # we can stop when l == r as r is max_r and hence it would just add 0 to result (line 23)
        while l < r:
            
            if h[l] < h[r]:
                if l_max < h[l]:
                    l_max = h[l]
                else:
                    result += l_max - h[l]
                l += 1
            else:
                if r_max < h[r]:
                    r_max = h[r]
                else:
                    result += r_max - h[r]
                r-= 1
        return result
                    
                