class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ans = [0] * len(temperatures)
        
        stack = []
        
        for idx, val in enumerate(temperatures):
            while stack and val > temperatures[stack[-1]]:
                j = stack.pop()
                ans[j] = idx - j
            stack.append(idx)
        return ans
            