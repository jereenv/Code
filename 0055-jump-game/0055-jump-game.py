class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        
        n = len(nums)
        notVis = [-1] * n
        
        def dp(idx):
            if idx >= n - 1:
                return True
            
            if notVis[idx] == 0:
                return False
            
            if nums[idx] == 0:
                return False
            
            for i in range(idx + nums[idx], idx, -1 ):
                if dp(i):
                    return True
                else:
                    notVis[idx] = 0
            
            return False
        
        return dp(0)
                
        
        