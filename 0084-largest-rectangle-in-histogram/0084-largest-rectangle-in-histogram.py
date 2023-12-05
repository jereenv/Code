class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        maxArea = 0
        stack  = []
        
        for idx, height in enumerate(heights):
            start = idx
            
            while stack and stack[-1][1] > height:
                s1, h1 = stack.pop(-1)
                maxArea = max(maxArea, (idx - s1) * h1)
                start = s1
            stack.append([start, height])
        
        while stack:
            s1, h1 = stack.pop(-1)
            maxArea = max(maxArea, (len(heights) - s1) * h1)
        return maxArea