class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        ones = 0
        for i in s:
            
            if i == "0":
                ans += ones
            else:
                ones += 1
        return ans
            
        
        