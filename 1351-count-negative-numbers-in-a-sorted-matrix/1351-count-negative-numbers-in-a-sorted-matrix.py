class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        ans = 0
        
        for arr in grid:
            ans +=  bisect_left(arr[::-1], 0)
        return ans
        