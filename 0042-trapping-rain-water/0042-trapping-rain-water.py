class Solution:
    def trap(self, h: List[int]) -> int:
        
        result = 0
        
        left_max = 0
        left_res = []
        for idx, h1 in enumerate(h):
            if h1 >= left_max:
                left_max = h1
                left_res.append(0)
            else:
                left_res.append(left_max - h1)
        
        right_max = 0
        right_res = []
        for i in reversed(range(len(h))):
            if h[i] >= right_max:
                right_max = h[i]
                right_res.append(0)
            else:
                right_res.append(right_max - h[i])
        
        s = 0
        
        for i in range(len(h)):
            s += min(left_res[i], right_res[len(h) - i - 1])
        
        return s
                
        