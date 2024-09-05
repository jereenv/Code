class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        s = sum(rolls)
        m = len(rolls)
        
        x = (mean * (m + n)) - s
        
        if x > 6 * n or x < n:
            return []
        
        t = x // n
        ans = [t] * n
        
        for i in range(x%n):
            ans[i] += 1
        return ans
        