class Solution:
    def trap(self, h: List[int]) -> int:
        
        result = 0
        
        left_max = list(h)
        for i in range(1,len(h)):
            left_max[i] = max(left_max[i], left_max[i - 1])
        
        right_max = list(h)
        for i in reversed(range(len(h) - 1)):
            right_max[i] = max(right_max[i], right_max[i+1])        
        
        for idx, h1 in enumerate(h):
            
            min_h = min(left_max[idx], right_max[idx])
            result += max(min_h - h1, 0)
        
        return result
                
        