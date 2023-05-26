class Solution:
    def rob(self, nums: List[int]) -> int:
        
        vis = {}
        def dp(i):
            if i <= 0:
                return nums[0]
            if i == 1:
                return nums[1]

            if i not in vis:
                vis[i] = nums[i] + max(dp(i-2), dp(i-3))
            print(vis,i)
            return vis[i]
        
        nums.append(0)
        return max(dp(len(nums)-1), dp(len(nums)-2))
        