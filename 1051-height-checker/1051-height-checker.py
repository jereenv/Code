class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        ans = 0
        
        for x, y in zip(heights, sorted(heights)):
            if x != y:
                ans += 1
        
        return ans
        