class Solution:
    def canJump(self, nums: List[int]) -> bool:
        notReach = set()
        
        def dp(idx):
            if idx in notReach:
                return False
            
            if idx >= len(nums) - 1:
                return True
            
            if nums[idx] == 0:
                return False
            
            canReach = dp(idx + 1)
            
            if canReach:
                return True
            
            for i in range(2, nums[idx] + 1):
                canReach = canReach or dp(idx + i)
            
            if not canReach:
                notReach.add(idx)
            
            return canReach
        
        return dp(0)
                
        
        