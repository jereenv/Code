class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        minDP = {}
        def dp(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if i not in minDP:
                minDP[i] = cost[i] + min(dp(i-1),dp(i-2))
            return minDP[i]
        
        cost.append(0)
        return dp(len(cost)-1)
        
        