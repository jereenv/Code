class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        n = len(nums)
        
        def dfs(idx, curr):
            if idx == n:
                ans.append(curr)
                return
            
            dfs(idx + 1, curr + [nums[idx]])
            dfs(idx + 1, curr)
            
        
        
        dfs(0, [])
        
        return ans
            
            
            
        