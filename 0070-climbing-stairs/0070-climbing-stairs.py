class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = {}
        def climb(n):
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n not in dp:
                dp[n] = climb(n-1) + climb(n-2)
            return dp[n]
        return climb(n)