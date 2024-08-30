class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = {}
        def dfs(idx, curr):
            if idx == n:
                return curr == target
            
            if (idx, curr) not in dp:
                dp[(idx, curr)] = dfs(idx + 1, curr + nums[idx]) + dfs(idx + 1, curr - nums[idx])

            return dp[(idx, curr)]
        
        return dfs(0, 0)