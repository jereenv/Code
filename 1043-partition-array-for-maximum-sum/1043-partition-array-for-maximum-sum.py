class Solution:
    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        memo = {}
        
        def dp(idx):
            if idx >= n:
                return 0
            
            if idx not in memo:
                temp = [max(arr[idx : idx + i]) * i + dp(idx + i) for i in range(1, min(k, n - idx) + 1)]
                memo[idx] = max(temp)
            return memo[idx]
        
        return dp(0)